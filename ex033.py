#Desafio33: Crie um programa que diga qual é o maior e o menor numero digitado pelo usuario.
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite o terceiro valor: '))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado doi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


