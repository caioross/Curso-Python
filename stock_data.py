import requests
import pandas as pd
import matplotlib.pyplot as plt

# Sua chave de API da Alpha Vantage
api_key = "sua_chave_api"

# Buscando os dados das ações
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=GOOGL&apikey={api_key}"
response = requests.get(url)
data = response.json()

# Convertendo os dados em um dataframe
df = pd.DataFrame(data["Time Series (Daily)"]).T
df.index = pd.to_datetime(df.index)

# Selecionando os dados dos últimos 30 dias
df = df.loc[df.index > (df.index[0] - pd.Timedelta(days=30))]

# Calculando a variação de cotação
df["variação"] = (df["4. close"].astype(float) - df["1. open"].astype(float)) / df["1. open"].astype(float)

# Ordenando as ações pelo maior lucro
df = df.sort_values("variação", ascending=False)

# Selecionando as 10 melhores ações
top_10 = df.head(10)

# Mostrando a tabela
print(top_10[["variação"]])

# Mostrando o gráfico
top_10["4. close"].astype(float).plot()
plt.show()
