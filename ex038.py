#Desafio38: crie um programa que leia 2 numeros inteiros e compare-os mostrando na tela a msg:
# o primeiro valor é maior, o segundo valor é maior ou  Nao existe valor maior, os dois sao iguais

a = int(input('Escreva um valor: '))
b = int(input('Escreva outro valor: '))

if a > b:
    print('O primeiro valor é maior')
elif b > a:
    print('O segundo valor é maior')
elif a == b:
    print('Nao existe valor maior, os dois sao iguais')

