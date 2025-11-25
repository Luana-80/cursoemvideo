#Desafio058: Melhore o jogo do desafio28 onde o comput vai pensar em um n. entre 0 e 10.
#sò que agora o jogador vai tentar advinhar ate acertar, mostrando no final qtos palpites precisou
# pra vencer.
from random import randint
computador = randint (0,10)
print('Sou seu computador... Acabei de pensar um n° entre 0 e 10')
print('Sera que voce consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez?')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!!!'.format(palpites))