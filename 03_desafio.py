""" DESAFIO """

# Perguntar o nome e ano de nascimento
# Retornar saudação com nome e idade.

nome = input("Qual o seu nome?")
anoNasc = input("Em que ano você nasceu?")
anoAtual = 2026
idade = anoAtual - int(anoNasc)

print("Olá " + nome + " você tem " + str(idade) + " anos")