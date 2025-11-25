#Crie um programa que leia o nome completo de uma pessoa e mostre: 1. o nome com todas as letras maiusculas;
# 2. todas minusculas; 3. qtas letras em considerar espaços;  4. qtas letras tem o primeiro nome.

nome = str(input('Escreva o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))