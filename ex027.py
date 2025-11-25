#Crie um programa que leia apenas o primeiro e o ultimo nome da pessoa
n = str(input('Escreva o seu nome completo: ')).strip().upper()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
