import json, requests

resultado = requests.get("https://minhaapi.caiorossi1.repl.co/total/")
dados = json.loads(resultado.text)
print("Total de vendas da unidade:")
print(dados['Total Vendas:'])

resultado = requests.get("https://minhaapi.caiorossi1.repl.co/media/")
dados = json.loads(resultado.text)
print("Media de vendas da unidade:")
print(dados['Media Vendas:'])

resultado = requests.get("https://minhaapi.caiorossi1.repl.co/composto/")
dados = json.loads(resultado.text)
print("Dados:")
print(dados['Media Vendas:'])
print(dados['Total Vendas:'])
