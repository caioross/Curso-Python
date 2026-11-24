executar = True
while executar :
    nome        = input("Digite seu nome:")
    anoAtual    = int(input("Digite o ano atual:"))
    anoNasc     = int(input("Digite o ano de nascimento:"))
    idade       = anoAtual - anoNasc
    print("Olá " + nome + "você tem " + str(idade) + " anos.")
    opcao = input("Você deseja testar novamente? \n[1] Sim ou [2] Não?")
    if opcao == "2" or opcao == "Não" or opcao == "não" or opcao == "nao" or opcao == "não" :
        executar = False