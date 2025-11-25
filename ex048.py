#Faça um programa que calcule a soma entre todos os numeros IMPARES multiplos de 3 entre 1 e 500:
soma = 0  # Variável para armazenar a soma
cont = 0
for num in range(1, 501, 2):  # Percorre apenas números ímpares de 1 a 500
    if num % 3 == 0:  # Verifica se é múltiplo de 3
        #print(num, end=' ')
        cont = cont + 1 #ou escreve cont += 1
        soma += num  # Soma o número à variável soma
print('A soma de todos os {} números ímpares múltiplos de 3 entre 1 e 500 é {}'.format(cont, soma))



