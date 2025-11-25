#Desafio18: Faça um programa que leia um angulo qqer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
'''import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o SENO {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem o COSSENO {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem a TANGENTE {:.2f}'.format(angulo, tangente))'''

from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
print('O angulo {} tem o SENO {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo {} tem o COSSENO {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem a TANGENTE {:.2f}'.format(angulo, tangente))