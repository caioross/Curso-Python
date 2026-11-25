
#        _           _     _
#   __ _(_)___   ___(_)___| |_ ___ _ __ ___   __ _ ___
#  / _` | / __| / __| / __| __/ _ \ '_ ` _ \ / _` / __|
# | (_| | \__ \ \__ \ \__ \ ||  __/ | | | | | (_| \__ \
#  \__,_|_|___/ |___/_|___/\__\___|_| |_| |_|\__,_|___/

# Autor: Nicole Prado
# Versão: 0.1.0

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import sqlite3
import os
import config
import numpy as np

app = Flask(__name__)
DB_PATH = 
db_path = 'dados.db'


# Função para inicializar o banco de dados
def init_db():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inadimplencia (
                mes TEXT PRIMARY KEY,
                inadimplencia REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS selic (
                mes TEXT PRIMARY KEY,
                selic_diaria REAL
            )
        ''')

        conn.commit()


@app.route('/')
def index():
    return render_template_string('''
        <h1>Upload de dados Econômicos</h1>

        <form action="/upload" method="POST"
              enctype="multipart/form-data">

            <label>Arquivo de Inadimplência (CSV):</label>
            <input name="campo_inadimplencia" type="file" required>

            <br><br>

            <label>Arquivo da Taxa Selic (CSV):</label>
            <input name="campo_selic" type="file" required>

            <br><br>

            <input type="submit" value="Fazer Upload">
        </form>

        <br><br>
        <hr>

        <a href="/consultar">Consultar dados Armazenados</a><br>
        <a href="/graficos">Visualizar Gráficos</a><br>
        <a href="/editar_inadimplencia">Editar dados de Inadimplência</a><br>
        <a href="/correlacao">Analisar Correlação</a>
    ''')


@app.route('/upload', methods=['POST'])
def upload():

    inad_file = request.files.get('campo_inadimplencia')
    selic_file = request.files.get('campo_selic')

    # Verificando os arquivos enviados
    if not inad_file or not selic_file:
        return jsonify({
            "Erro": "Ambos os arquivos precisam ser enviados"
        }), 400

    # Lendo os arquivos CSV
    inad_df = pd.read_csv(
        inad_file,
        sep=';',
        names=['data', 'inadimplencia'],
        header=0
    )

    selic_df = pd.read_csv(
        selic_file,
        sep=';',
        names=['data', 'selic_diaria'],
        header=0
    )

    # Convertendo as datas
    inad_df['data'] = pd.to_datetime(
        inad_df['data'], format="%d/%m/%y"
    )

    selic_df['data'] = pd.to_datetime(
        selic_df['data'], format="%d/%m/%y"
    )

    # Criando coluna de mês
    inad_df['mes'] = inad_df['data'].dt.to_period('M').astype(str)
    selic_df['mes'] = selic_df['data'].dt.to_period('M').astype(str)

    # Agrupando os dados mensalmente
    inad_mensal = (
        inad_df.groupby('mes')['inadimplencia']
        .mean()
        .reset_index()
    )

    selic_mensal = (
        selic_df.groupby('mes')['selic_diaria']
        .mean()
        .reset_index()
    )

    # Armazenando no banco SQLite
    with sqlite3.connect(db_path) as conn:

        inad_mensal.to_sql(
            'inadimplencia',
            conn,
            if_exists='replace',
            index=False
        )

        selic_mensal.to_sql(
            'selic',
            conn,
            if_exists='replace',
            index=False
        )

    return jsonify({
        'Mensagem': 'Dados armazenados com sucesso!'

    })
    
@app.route('/consultar', methods=['POST','GET'])
def consultar() :
    # Resultado se a pagina for carregada recebendo um POST]
    
    # Resultado sem receber um POST, ou seja, primeiro carregamento da pagina
    return render_template_string('''
        <h1> Consulta de tabelas </h1>
        <form method='POST'>
            <label for='campo tabela'> Escolha uma tabela: </label>
            <select name= 'campo tabela'>
                <option value='inadimplencia'> Inadimplencia </option>
                <option value= 'selic'> Taxa Selic </option>
            </select>
            <input type="submit" value="consultar">
        </form>
        <br><a  href="/"> Voltar </a>
    '''    )   


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
