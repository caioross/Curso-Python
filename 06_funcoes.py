
def minhaFuncao(curso) :
    print("Curso de " + curso + " na Clarify.")
    
minhaFuncao("Python")
minhaFuncao("SQL")
minhaFuncao("Claude")


cidades = ['São Paulo','Ribeirão Pires','Mauá','Cotia','Poá']
contador = 0

def minhaFuncaoMelhorada(item01, item02) :
    print(str(item02) + ' - ' + item01)     
    

for cidade in cidades :
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)
    
    
# alunos = ['Lucas', 'Rafael', 'Leonardo', 'Nicole', 'Caio']
# for lalala in alunos :
#     print(lalala)   