#Desafio16: Crie um programa que leia um n. real qualquer pelo teclado e mostre na tela a sua porçao inteira.

'''import math
num = float(input('Escreva um numero: '))
print('O numero {} tem a parte inteira {}'.format(num, math.trunc(num)))'''

num = float(input('Escreva um numero: '))
print('O numero {} tem a parte inteira {}'.format(num, int(num)))