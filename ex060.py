#Faça um programa que leia um numero qquer e mostre o seu fatorial. ex: %! = 5x4x3x2x1=120
from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'. format(n, f))

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculado {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c> 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
