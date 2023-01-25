print('Olá São Paulo')
#print('Caio "Super" Ross')
print( "Caio 'Super' Ross" )


# Isso é um comentario


'''
Isso é um comentario
de varias linhas
'''


print("Meu nome é: Caio.\nMeu curso é: Python")

"""Trabalhando com tipificação e **variaveis**"""

nome = "Caio" #string
sobrenome = "Ross" # isso é um comentario e jamais será interpretado
idade=35
altura = 1.81 #float
bermuda = False #boolean

print(nome + " " + sobrenome + " tem " + str(idade) + " anos")
print(idade + 2)

textoVariasLinhas = '''
operadores
soma +
subtracao - 
divisao /
multiplicacao *
potencia ^
exponenciação **
'''
print(textoVariasLinhas)

"""Detalhando strings e usando formato"""

nomeCompleto = "Caio Python Ross"
inicio = 5
fim =  inicio + 6
print(nomeCompleto[inicio:fim])

nome = input("Qual seu nome?")
sobrenome = input("Qual seu sobrenome")
print("Seu nome completo é: " + nome + " " + sobrenome)

valor01 = input("Insira seu primeiro valor: ")
valor02 = input("Insira seu segundo valor: ")

valor01 = int(valor01)

print(valor01 + int(valor02))

valor01 = input("Insira seu primeiro valor: ")
valor01 = input("Insira seu Segundo valor: ")

tipoEscola = input("Estuda em colegio: \n [1]Publico \n [2]Particular: \n")
mediaAluno = input("Qual a media do aluno?")
freqAluno = input("Qual a frequencia do aluno?")
mediaAluno = int(mediaAluno)
freqAluno = int(freqAluno)

# != diferente
# == igual
# <= menor ou igual
# >= maior ou igual
# > maior
# < menor

if tipoEscola == "2" :
  print("------- Colegio Particular --------")
  if mediaAluno >= 7 and freqAluno >= 70 :
    print("Aprovado")
  else :
    print("Reprovado")

if tipoEscola == "1" :
  print("-------- Colegio Publico --------")
  if mediaAluno >= 7 or freqAluno >= 70 :
    print("Aprovado")
  else :
    print("Reprovado")

print("fim")

palavra = "caio"
contador = 0
for letra in palavra :
  print(str(contador) + "-" + letra)
  contador = contador + 1

"""Projeto Calculadora"""

cidades = ['São Paulo','Guarulhos','Rio de Janeiro','Poá']
#print(cidades[0])

for cidade in cidades :
  print(cidade)

botaoExecutar = True
contador = 0
while botaoExecutar :
  print(contador)
  contador = contador + 1
  if contador >= 10 :
    botaoExecutar = False

def minhaFuncao() :
  print("lalala")

minhaFuncao()
minhaFuncao()

cidades = ['São Paulo','Guarulhos','Rio de Janeiro','Poá']
contador = 0

def minhaFuncaoMelhorada(informacao,x) :
  print(str(x) + ' - ' + informacao)

for cidade in cidades :
  contador = contador + 1
  minhaFuncaoMelhorada(cidade , contador)

executar = True
while executar :
  escolhas = '''
  Operações de calculo permitidas: 
  [1] ou [+] - Soma
  [2] ou [/] - Divisão
  [3] ou [*] - Multiplicação
  [4] ou [-] - Subtração
  [5] ou [**] - Potencia
  [0] ou [Sair] - Sair
  '''
  print(escolhas)
  operador = input("Selecione sua Opção")
  if operador == "0" or operador == "Sair":
    print("Obrigado por usar a Calculadora do SeuNome")
    executar = False
  else : 
    valor01 = input("Escolha seu primeiro valor")
    valor02 = input("Escolha seu segundo valor")

    valor01 = int(valor01)
    valor02 = int(valor02)

    if operador == "1" or operador == "+" :
      resultado = valor01 + valor02
      print("Resultado é: " + str(resultado))

    if operador == "2" :
      resultado = valor01 / valor02
      print("Resultado é: " + str(resultado))

    if operador == "3" :
      resultado = valor01 * valor02
      print("Resultado é: " + str(resultado))

    if operador == "4" :
      resultado = valor01 - valor02
      print("Resultado é: " + str(resultado))

    if operador == "5" :
      resultado = valor01 ** valor02
      print("Resultado é: " + str(resultado))

executar = True
while executar :
  escolhas = '''
    [1] ou [+] para Somar
    [2] ou [-] para Subtrair
    [3] ou [/] para Dividir
    [4] ou [*] para Multiplicar
    [5] para Sair
    (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)
  '''
  print(escolhas)
  operador = input("Qual sua opção?: ")
  valor01 = input("Escolha seu primeiro numero: ")
  valor02 = input("Escolha seu segundo numero: ")
  valor01 = int(valor01)
  valor02 = int(valor02)
  
  textinho02 = '''
      [1] Não, desejo sair!
      [2] Sim, desejo realizar outro calculo
    '''
  # Soma
  if operador == "1" or operador == "+" or operador == "Somar": 
    resultado = valor01 + valor02
    print("Resultado é: " + str(resultado))
    print(textinho02)
    operador = input("Deseja realizar outra conta?")
    if operador == "1" :
      executar = False



  # Subtração
  if escolha == "2" or escolha == "-" or escolha == "Subtrair":
    resultado = valor01 - valor02
    print("Resultado é: " + str(resultado))
    print(textinho02)
    escolha = input("Deseja realizar outra conta?")
    if escolha == "1" :
      executar = False


  # Divisão
  if escolha == "3" or escolha == "/" or escolha == "Dividir": 
    resultado = valor01 / valor02
    print("Resultado é: " + str(resultado))
    print(textinho02)
    escolha = input("Deseja realizar outra conta?")
    if escolha == "1" :
      executar = False

  # Multiplicação
  if escolha == "4" or escolha == "*" or escolha == "Multiplicar": 
    resultado = valor01 * valor02
    print("Resultado é: " + str(resultado))
    print(textinho02)
    escolha = input("Deseja realizar outra conta?")
    if escolha == "1" :
      executar = False

  # Sair
  if escolha == "5" or escolha == "Sair": 
    print("Obrigado por usar minha calculadora!")
    executar = False

escolha = input("Qual sua opção?: ")
#escolha = int(escolha)
#print(type(escolha))
if int(escolha) <= 0 or int(escolha) > 5 :
  executar = True

contador = input("Escolha um numero de 1 a 10")
contador = int(contador)

while (contador <= 10) :
  print(contador)
  contador = contador + 1

lojas = ['São Paulo','Rio de Janeiro','Belo Horizonte','curitiba']
#print(lojas[1])

for loja in lojas :
  print(loja)

for x in "Caio" :
  print(x)

contador = 0
teste = True
while teste :
  print(contador)
  contador = contador + 1
  if contador > 10 :
    teste = False

executar = True
while executar :
  anoNasci = int(input('Em que ano você nasceu?'))
  anoAtual = int(input('Em que ano estamos?'))
  idade = anoAtual - anoNasci
  print('Você tem:' + str(idade) + ' anos')
  opcao = input('\nDeseja testar novamente? \nSim ou não?')
  if opcao == "Não" or "N" or "Nao":
    executar = False
