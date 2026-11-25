#     _    ___ ____    ____  _     _                           
#    / \  |_ _/ ___|  / ___|(_)___| |_ ___ _ __ ___   __ _ ___ 
#   / _ \  | |\___ \  \___ \| / __| __/ _ \ '_ ` _ \ / _` / __|
#  / ___ \ | | ___) |  ___) | \__ \ ||  __/ | | | | | (_| \__ \
# /_/   \_\___|____/  |____/|_|___/\__\___|_| |_| |_|\__,_|___/

# Autor: Leonardo S Zambelli
# Versâo: 0.1.0

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import sqlite3
import os
import config 
import numpy as np

app=Flask(__name__)
db_path=config.DB_PATH

# Funcao para inicializar o banco de dados
def init_db():
    with sqlite3.connect(db_path) as conn:
        cursor=conn.cursor()
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
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Dashboard Econômico</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }

        body {
            min-height: 100vh;
            background:
                radial-gradient(circle at top left, #17345c, transparent 40%),
                linear-gradient(135deg, #08111f, #101e32 60%, #0b1728);
            color: #fff;
            padding: 45px 20px;
        }

        .container {
            max-width: 1050px;
            margin: auto;
        }

        /* CABEÇALHO */

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 45px;
            flex-wrap: wrap;
            gap: 20px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .logo {
            width: 52px;
            height: 52px;
            border-radius: 15px;
            background: linear-gradient(135deg, #00d4a0, #008cff);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 25px;
            box-shadow: 0 5px 25px #00d4a044;
        }

        .brand h2 {
            font-size: 19px;
            font-weight: 800;
        }

        .brand p {
            color: #8295ad;
            font-size: 12px;
            margin-top: 5px;
        }

        .status {
            background: #102c2b;
            color: #36e6b0;
            border: 1px solid #1d6654;
            border-radius: 30px;
            padding: 9px 16px;
            font-size: 12px;
        }

        /* TÍTULO */

        .hero {
            margin-bottom: 35px;
        }

        .hero span {
            color: #00d4a0;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .hero h1 {
            font-size: clamp(30px, 5vw, 43px);
            margin: 13px 0;
            font-weight: 800;
            letter-spacing: -1.5px;
        }

        .hero p {
            color: #91a3ba;
            font-size: 14px;
            line-height: 1.7;
        }

        /* ÁREA DE UPLOAD */

        .upload-card {
            background: rgba(20, 37, 59, 0.85);
            border: 1px solid #263d59;
            border-radius: 22px;
            padding: 32px;
            backdrop-filter: blur(15px);
            box-shadow: 0 20px 60px #00000030;
            margin-bottom: 35px;
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 25px;
        }

        .section-icon {
            background: #153c43;
            color: #00d4a0;
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .section-title h3 {
            font-size: 17px;
        }

        .section-title p {
            font-size: 12px;
            color: #8295ad;
            margin-top: 5px;
        }

        .upload-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .upload-box {
            background: #0e1d30;
            border: 1px dashed #38516d;
            border-radius: 16px;
            padding: 25px 20px;
            transition: .3s;
        }

        .upload-box:hover {
            border-color: #00d4a0;
            background: #12283a;
            transform: translateY(-3px);
        }

        .upload-box .file-icon {
            font-size: 27px;
            margin-bottom: 15px;
        }

        .upload-box h4 {
            font-size: 14px;
            margin-bottom: 8px;
        }

        .upload-box p {
            font-size: 11px;
            color: #8295ad;
            margin-bottom: 18px;
        }

        input[type="file"] {
            width: 100%;
            color: #a9bbd0;
            font-size: 11px;
        }

        input[type="file"]::file-selector-button {
            background: #1b3852;
            border: none;
            padding: 9px 12px;
            border-radius: 8px;
            color: #fff;
            cursor: pointer;
            margin-right: 8px;
        }

        input[type="file"]::file-selector-button:hover {
            background: #00a982;
        }

        .submit-btn {
            width: 100%;
            margin-top: 25px;
            padding: 16px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(90deg, #00c896, #008cff);
            color: white;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: .3s;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px #00c89640;
            filter: brightness(1.1);
        }

        /* MENU */

        .menu-title {
            font-size: 17px;
            margin-bottom: 18px;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .menu-item {
            text-decoration: none;
            color: white;
            background: #14253b;
            border: 1px solid #263d59;
            padding: 22px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            gap: 16px;
            transition: .3s;
        }

        .menu-item:hover {
            border-color: #00d4a0;
            background: #192f47;
            transform: translateY(-4px);
        }

        .menu-icon {
            width: 46px;
            height: 46px;
            border-radius: 13px;
            background: #1d3850;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 21px;
        }

        .menu-item h4 {
            font-size: 13px;
            margin-bottom: 6px;
        }

        .menu-item p {
            font-size: 11px;
            color: #8295ad;
        }

        .arrow {
            margin-left: auto;
            color: #00d4a0;
            font-size: 20px;
        }

        footer {
            text-align: center;
            color: #536982;
            font-size: 11px;
            margin-top: 45px;
        }

        /* RESPONSIVIDADE */

        @media (max-width: 650px) {
            body {
                padding: 25px 15px;
            }

            .upload-grid,
            .menu-grid {
                grid-template-columns: 1fr;
            }

            .upload-card {
                padding: 22px 17px;
            }

            .hero h1 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <header class="header">
        <div class="brand">
            <div class="logo">📊</div>

            <div>
                <h2>ECON DATA</h2>
                <p>Economic Intelligence Platform</p>
            </div>
        </div>

        <div class="status">● Sistema de análise</div>
    </header>


    <section class="hero">
        <span>PAINEL DE CONTROLE</span>

        <h1>Dados Econômicos</h1>

        <p>
            Gerencie, consulte e analise indicadores econômicos
            em um único ambiente.
        </p>
    </section>


    <section class="upload-card">

        <div class="section-title">
            <div class="section-icon">⇧</div>

            <div>
                <h3>Importação de dados</h3>
                <p>Faça upload dos arquivos CSV para atualizar sua base de dados.</p>
            </div>
        </div>

        <form action="/upload" method="POST" enctype="multipart/form-data">

            <div class="upload-grid">

                <div class="upload-box">
                    <div class="file-icon">📉</div>

                    <h4>Dados de Inadimplência</h4>

                    <p>Selecione o arquivo CSV de inadimplência.</p>

                    <input
                        type="file"
                        name="campo_inadimplencia"
                        accept=".csv"
                        required
                    >
                </div>


                <div class="upload-box">
                    <div class="file-icon">📈</div>

                    <h4>Taxa SELIC</h4>

                    <p>Selecione o arquivo CSV da taxa SELIC.</p>

                    <input
                        type="file"
                        name="campo_selic"
                        accept=".csv"
                        required
                    >
                </div>

            </div>

            <button type="submit" class="submit-btn">
                ↑ &nbsp; Fazer upload dos arquivos
            </button>

        </form>

    </section>


    <section>

        <h3 class="menu-title">Ferramentas de análise</h3>

        <div class="menu-grid">

            <a href="/consultar" class="menu-item">
                <div class="menu-icon">🗄️</div>

                <div>
                    <h4>Consultar dados</h4>
                    <p>Visualize os dados armazenados.</p>
                </div>

                <span class="arrow">›</span>
            </a>


            <a href="/graficos" class="menu-item">
                <div class="menu-icon">📊</div>

                <div>
                    <h4>Visualizar gráficos</h4>
                    <p>Explore indicadores econômicos.</p>
                </div>

                <span class="arrow">›</span>
            </a>


            <a href="/editar_inadimplencia" class="menu-item">
                <div class="menu-icon">✏️</div>

                <div>
                    <h4>Editar inadimplência</h4>
                    <p>Gerencie os registros da base.</p>
                </div>

                <span class="arrow">›</span>
            </a>


            <a href="/correlacao" class="menu-item">
                <div class="menu-icon">🔗</div>

                <div>
                    <h4>Analisar correlação</h4>
                    <p>Compare SELIC e inadimplência.</p>
                </div>

                <span class="arrow">›</span>
            </a>

        </div>

    </section>


    <footer>
        ECON DATA © 2026 — Plataforma de Inteligência Econômica
    </footer>

</div>

</body>
</html>                            
    ''')

@app.route('/upload', methods=['POST','GET]'])    
def upload(): 
    inad_file=request.files.get('campo_inadimplencia')
    selic_file=request.files.get('campo_selic')
    
    #vamos verificar se os arquivos foram devidamente enviados
    if not inad_file or not selic_file:
        return jsonify({"Erro" : "Ambos os arquivos precisam ser enviados!"})
    inad_df = pd.read_csv(
        inad_file,
        sep=';',
        names = ['data', 'inadimplencia'],
        header=0
    )
    selic_df = pd.read_csv(
        selic_file,
        sep=';',
        names = ['data', 'selic_diaria'],
        header=0
    )
    inad_df['data']=pd.to_datetime(inad_df['data'],format="%d/%m/%Y")
    selic_df['data']=pd.to_datetime(selic_df['data'],format="%d/%m/%Y")
    inad_df['mes']=inad_df['data'].dt.to_period('M').astype(str)
    selic_df['mes']=selic_df['data'].dt.to_period('M').astype(str)
    
    inad_mensal = inad_df[['mes','inadimplencia']].drop_duplicates()
    selic_mensal = selic_df.groupby('mes')['selic_diaria'].mean().reset_index()
    
    with sqlite3.connect(db_path) as conn:
        inad_mensal.to_sql('inadimplencia', conn, if_exists='replace',index=False)
        selic_mensal.to_sql('selic', conn, if_exists='replace',index=False)
    return jsonify({'Mensagem':'dados armazenados com sucesso!'})    
    
@app.route('/consultar', methods=['POST','GET'])
def consultar ():
    #resultado se a pagina for carregada recebendo um POST
    if request.method == 'POST': 
        tabela=request.form.get('campo_tabela')
        if tabela not in ['inadimplencia', 'selic']:
            return jsonify ({'Erro': 'Tabela Invalida'}),400
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(f'SELECT * FROM {tabela}', conn) 
            return df.to_html(index=False)
    #resultado sem receber um POST, ou seja, primeiro carregamento da pagina
    return render_template_string ('''
        <h1> Consulta de Tabela </h1>
        <form method='POST'>
            <label for='campo_tabela'> Escolha uma Tabela: </label>
            <select name='campo_tabela'>
                <option values='inadimplencia'> Inadimplencia </option>
                <option values='selic' > Taxa Selic </option>
            </select>
            <input type="submit" value="consultar">
            </form>
            <br><a href="/">Voltar</a>
                                   
    ''')
    
if __name__== '__main__':
    init_db()
    app.run(debug=True)