nome = str(input('Qual o seu nome: ')).upper()
if nome == 'LUANA':
    print('Que nome lindo voce tem')
else:
    print('Seu nome é tao normal...')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2)/2
print('Sua média foi {}'.format(m))

if m >=6.0:
    print('Que nota boa! PARABENS!')
else:
    print('Sua nota foi ruim. ESTUDE MAIS!')

#print('PARABENS!' if m>=6 else 'ESTUDE MAIS!')