!pip install requests
import requests

def lala():
	print('CEPython')

	cep = input('Digite o CEP para a consulta: ')
	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
	endereco = request.json()

	print('==> CEP ENCONTRADO <==')
	print('CEP: {}'.format(endereco['cep']))
	print('Cidade: {}'.format(endereco['localidade']))
	print(f"Estado: {endereco['uf']}")

lala()
