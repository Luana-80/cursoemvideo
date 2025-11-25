#Desenvolva um programa que leia o 1o termo e a razao de uma progressao aritmetica.
# no final mostre os 10 primeiros termos dessa progressao.
print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' *30)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' - ')
print('ACABOU')

