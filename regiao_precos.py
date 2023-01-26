import pandas as pd 
import matplotlib.pyplot as plt 

# Definindo o formato da fonte de dados e as colunas
df = pd.read_csv('precos_casa1.csv', delimiter=',', decimal='.', encoding='utf-8')
df.columns=['Regiao', 'Preco']

# Um simples histograma dos preços das casas
df['Preco'].plot.hist(bins = 30, color ='green', edgecolor = 'black')

# Calculando estatísticas
print('A estatística descritiva da variável Preço:')
print(df.describe())

# Agrupando os dados por região
df_regiao = df.groupby('Regiao') 
print('\nA média dos preços por região:')
print(df_regiao.mean())

# Obtendo o preço máximo e a região correspondente
preco_max = df_regiao['Preco'].max()
regiao_max = df_regiao['Preco'].idxmax()

print('\nA região com o preço máximo da casa é', regiao_max[0],
      'com um valor de', preco_max[0])

# Dica: gere um arquivo CSV com os dados
df.to_csv('dados_precos.csv', index=False)

print('\nVocê gerou um arquivo CSV com os dados para analisar mais profundamente os preços das casas por região!')
