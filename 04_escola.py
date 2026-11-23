# != Diferente
# == Igual
# > Maior
# < Menor
# >= Maior ou igual
# <= Menor ou igual


tipoEscola = input("Qual o tipo do colegio: \n [1] Publico \n [2] Particular: \nR:")
mediaAluno = int(input("Qual a média do aluno: \nR: "))
freqAluno = int(input("Qual a frequencia do aluno: \nR: "))
mediaCorte = 7
freqCorte = 70

if tipoEscola == "2" :
    if mediaAluno >= mediaCorte and freqAluno >= freqCorte :
        print("Aprovado")
    else :
        print("Reprovado")

if tipoEscola == "1" :
    if mediaAluno >= 5 or freqAluno >= freqCorte :
        print("Aprovado")
    else :
        print("Reprovado")