import random

def construirbaralho():
    baralho = []
    # example carta:Red 7,Green 8, Blue pular
    cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
    valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "virar dois", "pular", "inverter"]
    coringas = ["coringa", "coringa virar quatro"]
    for cores in cores:
        for valor in valores:
            cartaVal = "{} {}".format(cores, valor)
            baralho.append(cartaVal)
            if valor != 0:
                baralho.append(cartaVal)
    for i in range(4):
        baralho.append(coringas[0])
        baralho.append(coringas[1])
    print(baralho)
    return baralho


def embaralharbaralho(baralho):
    for cartapos in range(len(baralho)):
        aleatorio = random.randint(0, 107)
        baralho[cartapos], baralho[aleatorio] = baralho[aleatorio], baralho[cartapos]
    return baralho




def virarcartas(numcartas):
    virarcarta = []
    for x in range(numcartas):
        virarcarta.append(unobaralho.pop(0))
    return virarcarta


def showHand(jogador, maojogador):
    print("jogador {} sua vez".format(jogadores_nome[jogador]))
    print("Sua mão")
    print("------------------")
    y = 1
    for carta in maojogador:
        print("{}) {}".format(y, carta))
        y += 1
    print("")


def podejogar(cores, valor, maojogador):

    for carta in maojogador:
        if "coringa" in carta:
            return True
        elif cores in carta or valor in carta:
            return True
    return False


unobaralho = construirbaralho()
unobaralho = embaralharbaralho(unobaralho)
unobaralho = embaralharbaralho(unobaralho)
descarte = []

jogadores_nome = []
jogadores = []
cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
numjogadores = int(input("Quantos jogadores?"))
while numjogadores < 2 or numjogadores > 4:
    numjogadores = int(
        input("Invalido, escolha quantos jogadores?"))
for jogador in range(numjogadores):
    jogadores_nome.append(input("Enter jogador {} nome: ".format(jogador+1)))
    jogadores.append(virarcartas(5))


jogadorvez = 0
direcao = 1
jogando = True
descarte.append(unobaralho.pop(0))
trocacarta = descarte[0].split(" ", 1)
atualcores = trocacarta[0]
if atualcores != "coringa":
    cartaVal = trocacarta[1]
else:
    cartaVal = "Qualquer"

while jogando:
    showHand(jogadorvez, jogadores[jogadorvez])
    print("carta no topo do baralho: {}".format(descarte[-1]))
    if podejogar(atualcores, cartaVal, jogadores[jogadorvez]):
        cartaEscolhida = int(input("Que carta quer jogar?"))
        while not podejogar(atualcores, cartaVal, [jogadores[jogadorvez][cartaEscolhida-1]]):
            cartaEscolhida = int(
                input("Invalido escolha uma carta?"))
        print("Você Jogou {}".format(jogadores[jogadorvez][cartaEscolhida-1]))
        descarte.append(jogadores[jogadorvez].pop(cartaEscolhida-1))

        if len(jogadores[jogadorvez]) == 0:
            jogando = False
            vencedor = jogadores_nome[jogadorvez]
        else:

            trocacarta = descarte[-1].split(" ", 1)
            atualcores = trocacarta[0]
            if len(trocacarta) == 1:
                cartaVal = "Qualquer"
            else:
                cartaVal = trocacarta[1]
            if atualcores == "coringa":
                for x in range(len(cores)):
                    print("{} {}".format(x+1, cores[x]))
                novocores = int(
                    input("Escolha uma cor "))
                while novocores < 1 or novocores > 4:
                    novocores = int(
                        input("Invalido, escolha uma cor"))
                atualcores = cores[novocores-1]
            if cartaVal == "inverter":
                direcao = direcao * -1 
            elif cartaVal == "pular":
                jogadorvez += direcao
                if jogadorvez >= numjogadores:
                    jogadorvez = 0
                elif jogadorvez < 0:
                    jogadorvez = numjogadores-1
            elif cartaVal == "Comprar +2":
                jogadorvirar = jogadorvez+direcao
                if jogadorvirar == numjogadores:
                    jogadorvirar = 0
                elif jogadorvirar < 0:
                    jogadorvirar = numjogadores-1
                jogadores[jogadorvirar].extend(virarcartas(2))
            elif cartaVal == "Comprar +4":
                jogadorvirar = jogadorvez+direcao
                if jogadorvirar == numjogadores:
                    jogadorvirar = 0
                elif jogadorvirar < 0:
                    jogadorvirar = numjogadores-1
                jogadores[jogadorvirar].extend(virarcartas(4))
            print("")
    else:
        print("Você deve descartar uma carta.")
        jogadores[jogadorvez].extend(virarcartas(1))

    jogadorvez += direcao
    if jogadorvez >= numjogadores:
        jogadorvez = 0
    elif jogadorvez < 0:
        jogadorvez = numjogadores-1

print("Game Over")
print("{} venceu!".format(vencedor))
