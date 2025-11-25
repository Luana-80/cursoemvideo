#Faça um programa que leia um n. de 0 a 9999 e mostre na tela cada um dos digitos separados.
#este sistema deu erro porque se digitar apenas 3 numeros ele trava:
'''num = int(input('digite um numero: '))
n = str(num)
print('unidade {}: '.format(n[3]))
print('dezema {}: '.format(n[2]))
print('centena {}: '.format(n[1]))
print('milhar {}: '.format(n[0]))'''

#utilizando a matematica:
num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade {}: '.format(u))
print('dezema {}: '.format(d))
print('centena {}: '.format(c))
print('milhar {}: '.format(m))