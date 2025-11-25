#Desafio5: Faça um programa que leia um numero inteiro e mostre na tela do seu sucessor e seu antecessor
n = int(input('Escreva um numero: '))
a = n - 1
s = n + 1
print('O numero escolhido é {}, seu antecessor é {}, e seu antecessor é {}'.format(n, a, s))

#outra forma de escrever este programa, economizando memoria, porém, se precisasse das variaveis nao daria certo
n = int(input('Escreva um numero: '))
print('O numero escolhido é {}, seu antecessor é {}, e seu sucessor é{}'.format(n, (n-1), (n+1)))


