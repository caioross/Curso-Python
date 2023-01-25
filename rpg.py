import random

# Criação do jogador
jogador = {"nome": "", "vida": 100, "ataque": 10, "defesa": 5}

# Criação dos monstros
monstros = [{"nome": "Goblin", "vida": 50, "ataque": 5, "defesa": 2}, 
            {"nome": "Orc", "vida": 75, "ataque": 8, "defesa": 4},
            {"nome": "Dragão", "vida": 100, "ataque": 15, "defesa": 10}]

# Função para movimentar o jogador
def mover(direcao):
    if direcao == "norte":
        print("Movendo para o norte...")
    elif direcao == "sul":
        print("Movendo para o sul...")
    elif direcao == "leste":
        print("Movendo para o leste...")
    elif direcao == "oeste":
        print("Movendo para o oeste...")
    else:
        print("Movimento inválido.")

# Função para batalhar com um monstro
def batalhar(monstro):
    print("Iniciando batalha contra o {}...".format(monstro["nome"]))
    while jogador["vida"] > 0 and monstro["vida"] > 0:
        jogador["vida"] -= max(0, monstro["ataque"] - jogador["defesa"])
        monstro["vida"] -= max(0, jogador["ataque"] - monstro["defesa"])
        print("Jogador: {}/{} | {}: {}/{}".format(jogador["nome"], jogador["vida"], monstro["nome"], monstro["vida"], monstro["defesa"]))
    if jogador["vida"] > 0:
        print("Você venceu a batalha!")
    else:
        print("Você foi derrotado.")

# Obtendo o nome do jogador
jogador["nome"] = input("Digite o nome do jogador: ")

# Loop principal do jogo
while jogador["vida"] > 0:
    comando = input("O que deseja fazer? (mover, batalhar, sair) ").lower()
    if comando == "mover":
        direcao = input("Para qual direção deseja mover? (norte, sul, leste, oeste) ").lower()
        mover(direcao)
    elif comando == "batalhar":
        monstro = random.choice(monstros)
        batalhar(monstro)
    elif comando == "sair":
        break
    else:
        print("Comando inválido.")
