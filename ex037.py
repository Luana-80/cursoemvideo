#Desafio37: Escreva um programa que leia um n inteiro e peça para escolher a base de conversao:
#1 para binario, 2 para octal ou 3 para hexadecimal

numero = int(input('Escreva um numero: '))
escolha = int(input('Escreva 1 para binario, 2 para octal ou 3 para hexadecimal: '))

if escolha == 1:
    print('O numero {} no sistema binario é {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O numero {} no sistema octal é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O numero {} no sistema hexadecimal é {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('Opcao invalida! Escolha 1, 2 ou 3')
