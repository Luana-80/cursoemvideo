#Desenvolva um programa que leia seis n. inteiros e mostre a soma apenas dos PARES.
# Se for impar desconsidere.
s = 0
for c in range(0, 6): #Loop para ler 6 numeros
    num = int(input('Digite um valor: '))
    if num % 2 == 0: #verifica se o n. è PAR
        s += num #soma apenas os pares
print('O somatorio dos valores PARES é {}'.format(s))