from flask  import Flask, redirect, url_for, request, render_template, jsonify
# from requests import get
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('inicio.html')

@app.route('/login')
def fazer_login():
    return render_template('login.html')

@app.route('/pagina403')
def pagina403():
    return render_template('pagina403.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/validador/', methods=['POST', 'GET'])
def validador():
    acesso_u = 'caio'
    acesso_s = '123'
    if request.method == "POST" :
        usuario = request.form['c_usuario']
        senha = request.form['c_senha']
        #usuario, senha = request.form['c_usuario', 'c_senha']
        if usuario == acesso_u and senha == acesso_s :
            return redirect(url_for('welcome'))
        else :
            return redirect(url_for('pagina403'))
    else :
        usuario = request.args.get('c_usuario') 
        senha =  request.args.get('c_senha')
        if usuario == acesso_u and senha == acesso_s :
            return redirect(url_for('welcome'))
        else :
            return redirect(url_for('pagina403'))
    
@app.route('/consultar_ibge/<nome>', methods=['GET'])
def consultar_ibge(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    resposta = requests.get(url)
    
    #resposta.raise_for_status()
    
    dados = resposta.json()
    
    if not dados or not dados[0].get('res') :
        return jsonify({'Erro':'Nome não encontrado!'}), 404
    
    # pegando os dados internos
    df = pd.DataFrame(dados[0]['res'])
    
    # criando o grafico
    fig, ax = plt.subplots(figsize=(10,5))
    
    ax.bar(
        df['periodo'],
        df['frequencia'],
        color = 'royalblue'
    )
    ax.set_xlabel('Década')
    ax.set_ylabel('Frequencia')
    ax.set_title(f'Frequencia do {nome} no Brasil')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Convertendo o grafico em imagem
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    grafico = base64.b64encode(img.getvalue()).decode("utf-8")
    
    plt.close(fig)
    
    return f'<h1>Consulta IBGE: {nome}</h1><img src="data:image/png;base64, {grafico}">' 
    
if __name__ == '__main__':
    app.run(debug=True)