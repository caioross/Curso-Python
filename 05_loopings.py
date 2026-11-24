palavra = "Caio"
contador = 1

for letra in palavra :
    print( str(contador) + "-" + letra)
    contador = contador + 1
    
cidades = ['São Paulo','Ribeirão Pires','Mauá','Cotia','Poá']
print(cidades[0])

for cidade in cidades : 
    print(cidade)
    
botaoExecutar = True
contador = 0
while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False