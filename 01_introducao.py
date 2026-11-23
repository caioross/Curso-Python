print("Olá 'São' Paulo")
# print('Olá "São" Paulo')

'''
Isso é um comentario
de varias linhas
'''

print("Meu nome é: Caio. \nMeu Curso é: Python")

nome = "Caio" # String / Texto
idade = 38 # Tipo Integer
idadeErrada = "38"
altura = 1.81 # Float
ligaDesliga = True # ou False / São Booleans
textoVariasLinhas = '''
                    Posso escrever
                    Um monte de
                    informação aqui!
                    '''
print(textoVariasLinhas)

print("Meu nome é " + nome)

resultado = idade + idade
print(resultado) # Mostra: 76

resultado = idadeErrada + idadeErrada
print(resultado) # Mostra: 3838

resultado = "alterei o resultado pela terceira vez!"
print(resultado) # Mostra: alterei o resultado pela terceira vez!


print("Meu nome é:" + nome + " e tenho " + str(idade) + " anos.")
