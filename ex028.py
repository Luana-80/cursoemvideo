#Desafio28 - tente advinhar um numero entre 0 e 5 do computador
from random import randint
from time import sleep
computador = randint (0,5)
print('---' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('---' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! VOCE VENCEU!')
else:
    print('PERDEU! Pensei no {} e voce escolheu o {} '.format(computador, jogador))
