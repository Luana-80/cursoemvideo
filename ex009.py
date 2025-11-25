#Desafio9: Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um numero para ver sua tabuada = '))
a = n * 1
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10
print('============ \n {} * 1 = {} \n {} * 2 = {} \n {} * 3 = {} \n {} * 4 = {} \n {} * 5 = {} \n {} * 6 = {} \n {} * 7 = {} \n {} * 8 = {} \n {} * 9 = {} \n {} * 10 = {} \n============' .format(n, a, n, b, n, c, n, d, n, e, n, f, n, g, n, h, n, i, n, j))

#outra maneira de fazer
num = int(input('Digite um numero para ver sua tabuada: '))
print('-' *12)
print('{} * {:2} = {}'. format(num, 1, (num*1)))
print('{} * {:2} = {}'. format(num, 2, (num*2)))
print('{} * {:2} = {}'. format(num, 3, (num*3)))
print('{} * {:2} = {}'. format(num, 4, (num*4)))
print('{} * {:2} = {}'. format(num, 5, (num*5)))
print('{} * {:2} = {}'. format(num, 6, (num*6)))
print('{} * {:2} = {}'. format(num, 7, (num*7)))
print('{} * {:2} = {}'. format(num, 8, (num*8)))
print('{} * {:2} = {}'. format(num, 9, (num*9)))
print('{} * {} = {}'. format(num, 10, (num*10)))
print('-' *12)

