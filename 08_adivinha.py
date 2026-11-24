#     _    ______     _____ _   _ _   _    _       ____    _    __  __ _____ 
#    / \  |  _ \ \   / /_ _| \ | | | | |  / \     / ___|  / \  |  \/  | ____|
#   / _ \ | | | \ \ / / | ||  \| | |_| | / _ \   | |  _  / _ \ | |\/| |  _|  
#  / ___ \| |_| |\ V /  | || |\  |  _  |/ ___ \  | |_| |/ ___ \| |  | | |___ 
# /_/   \_\____/  \_/  |___|_| \_|_| |_/_/   \_\  \____/_/   \_\_|  |_|_____|
#
# AUTOR: Caio Comirte Rossi
# VERSÃO: 1.0.0
# LICENÇA: OPEN SOURCE

from random import randint

random = randint(1, 100)
chute = 0
chances = 10

while chute != random :
    chute = input('Chute um numero de 0 a 100:')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('')
            print('Parabéns! Você venceu! O numero era {} e você ainda {} chances.'.format(random, chances ))
            print('')
            break
        else :
            print('')
            if chute > random:
                print('Você errou! Dica: É um numero menor')
            else :
                print('Você errou! Dica: É um numero maior')
            print(f'Você ainda tem {chances} chances.')
            print('')
        if chances == 0 :
            print('')
            print('Suas chances acabaram, voce perdeu o numero era: {}'.format(random))
            print('')
            break
print('GAME OVER')
        
            




