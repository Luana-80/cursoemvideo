from random import randint
from time import sleep

item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

# Validação antes de continuar
if jogador not in [0, 1, 2]:
    print('JOGADA INVÁLIDA!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 11)
    print(f'O computador escolheu {item[computador]}')
    print(f'O jogador escolheu {item[jogador]}')
    print('-=' * 11)

    if computador == jogador:
        print('EMPATE!')
    elif (computador == 0 and jogador == 1) or \
         (computador == 1 and jogador == 2) or \
         (computador == 2 and jogador == 0):
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')


