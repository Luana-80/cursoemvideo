#Refaça o ex009 mostrando a tabuada de um n. que o usuario escolher, so que agora com laço FOR

num = int(input('Digite um numero para ver sua tabuada: '))
print('Tabuada do {}'.format(num))
for c in range(1, 11):
    print('{} x {:2} = {:3}'. format(num, c, (num * c)))
