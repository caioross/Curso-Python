from flask import Flask, request, jsonify
import requests
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/consultar_ibge/<string:nome>", methods=["GET"])
def consultar_ibge(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.bar(df["localidade"], df["frequencia"])
    ax.set_xlabel("Localidade")
    ax.set_ylabel("Frequência")
    plt.show()

if __name__ == "__main__":
    app.run(debug=True)
