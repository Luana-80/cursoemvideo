print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' *20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    if a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')
