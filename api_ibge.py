import json, requests

response = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/caio")


json_data = json.loads(response.text)

print(json_data[0]['res'][0])
