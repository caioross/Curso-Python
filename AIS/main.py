#     _    ___ ____    ____  _     _                           
#    / \  |_ _/ ___|  / ___|(_)___| |_ ___ _ __ ___   __ _ ___ 
#   / _ \  | |\___ \  \___ \| / __| __/ _ \ '_ ` _ \ / _` / __|
#  / ___ \ | | ___) |  ___) | \__ \ ||  __/ | | | | | (_| \__ \
# /_/   \_\___|____/  |____/|_|___/\__\___|_| |_| |_|\__,_|___/

# Autor: Caio C Rossi
# Versão: 0.1.0

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import sqlite3
import os
import config
import numpy as np

app = Flask(__name__)
db_path = config.DB_PATH

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
    <h1> Upload de dados Econômicos </h1>
        <form action='/upload' method='POST' enctype='multipart/form-data'>
            <label for='campo_inadimplencia'> Aquivo de Inadimplência (CSV): </label>    
            <input name='campo_inadimplencia' type='file' required><br><br>
                                  
            <label for='campo_selic'> Arquivo da Taxa Selic (CSV) </label>
            <input name="campo_selic" type='file' required> <br/> <br/>
            <input type='submit' value='Fazer Upload'>
        </form>
        <br><br>
        <hr>
        <a href='/consultar'> Consultar dados Armazenados </a><br>
        <a href='/graficos'> Visualizar Graficos </a><br>
        <a href='/editar_inadimplencia'> Editar dados de Inadimplencia </a><br>
        <a href='/correlacao'> Analisar Correlação </a><br>                                                      
    ''')

@app.route('/upload', methods=['POST','GET'])
def upload():
    inad_file = request.files.get('campo_inadimplencia')
    selic_file = request.files.get('campo_selic')
    
    # Vamos verificar se os arquivos foram devidamentte enviados
    if not inad_file or not selic_file:
        return jsonify({"Erro":"Ambos os arquivos precisam ser enviados!"})
    inad_df = pd.read_csv(
        inad_file,
        sep = ';',
        names = ['data', 'inadimplencia'],
        header = 0
    )
    selic_df = pd.read_csv(
        selic_file,
        sep = ';',
        names = ['data', 'selic_diaria'],
        header = 0
    )
    
    inad_df['data'] = pd.to_datetime(inad_df['data'], format="%d/%m/%Y")
    selic_df['data'] = pd.to_datetime(selic_df['data'], format="%d/%m/%Y")
    
    inad_df['mes'] = inad_df['data'].dt.to_period('M').astype(str)
    selic_df['mes'] = selic_df['data'].dt.to_period('M').astype(str)
    
    inad_mensal = inad_df[['mes','inadimplencia']].drop_duplicates()
    selic_mensal = selic_df.groupby('mes')['selic_diaria'].mean().reset_index()
    
    with sqlite3.connect(db_path) as conn :
        inad_mensal.to_sql('inadimplencia', conn, if_exists='replace', index = False)
        selic_mensal.to_sql('selic', conn, if_exists='replace', index = False)
    return jsonify({'Mensagem':'dados armazenados com sucesso!'})

@app.route('/consultar', methods=['POST','GET'])
def consultar() :
    # Resultado se a pagina for carregada recebendo um POST
    if request.method == 'POST' :
        tabela = request.form.get('campo_tabela')
        if tabela not in ['inadimplencia','selic'] :
            return jsonify({'Erro':'Tabela inválida'}),400
        with sqlite3.connect(db_path) as conn :
            df = pd.read_sql_query(f'SELECT * FROM {tabela}', conn)
        return df.to_html(index=False)
        
    
    # Resultado sem receber um POST, ou seja, primeiro carregamento da pagina
    return render_template_string('''
        <h1> Consulta de Tabelas </h1>
        <form method='POST'>
            <label for='campo_tabela'> Escolha uma Tabela: </label>
            <select name='campo_tabela'>
                <option value='inadimplencia'> Inadimplencia </option>
                <option value='selic'> Taxa Selic </option>
            </select>
            <input type="submit" value="consultar">
        </form>       
        <br><a  href="/"> Voltar </a>             
    ''')
    
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)