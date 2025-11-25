#Desafio35: Crie um programa que analise se 3 retas podem ou nao se tornar um triangulo
print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' *20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Os segmentos acima PODEM FORMAR um triangulo')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')
