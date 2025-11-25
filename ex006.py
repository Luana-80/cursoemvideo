#Desafio6: Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Escreva um numero ='))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Meu numero é {}, seu dobro é {}, seu triplo é {}, e a raiz quadrada de {} é {:.2f}'. format(n, d, t, n, r))