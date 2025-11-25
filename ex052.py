#Faça um programa que leia um n. inteiro e diga se ele é ou nao um n. PRIMO
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot ==2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NAO é PRIMO!')