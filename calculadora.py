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
