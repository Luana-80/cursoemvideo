#Estrutura de repetiçao FOR, laços de repetiçao:
for c in range(0,6):
    print('Estudar Python!') #imprime o texto 6x
print('FIM') #esta estrutura està fora do laço, por isso ela escreve uma vez apenas
print('=' *20)
for c in range(0,6):
    print(c)  # numera em ordem crescente
print('=' *20)
for c in range(6, 0, -1): #numera em ordem decrescente
    print(c)
print('=' *20)
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')
print('=' *20)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('=' *20)
for c in range(0, 10): #vai abrir para o usuario escrever 10x
    n = int(input('Digite um valor: '))
print('FIM')
print('=' *20)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))
