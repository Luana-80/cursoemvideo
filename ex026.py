#Faça um programa que leia uma frase pelo teclado e mostre qtas vezes aparece o A, em que posiçao aparece a 1a vez, em que posiçao aparece a ultima vez
frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posiçao {}'.format(frase.find('A')+1))
print('A letra A aparece a ultima vez na posiçao {}'.format(frase.rfind('A')+1))
