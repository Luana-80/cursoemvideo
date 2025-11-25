import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de um {} arredondando pra cima é igual a {}'.format(num,math.ceil(raiz)))
print('A raiz de um {} arredondando pra baixo é igual a {}'.format(num,math.floor(raiz)))


#from math import sqrt, floor
#num = int(input('Digite um numero: '))
#raiz = sqrt(num)
#print('A raiz de um {} é igual a {:.2f}'.format(num, floor(raiz)))

import random
num = random.randint(1,60)
print(num)

import emoji
print(emoji.emojize('Python is :thumbs_up:'))


