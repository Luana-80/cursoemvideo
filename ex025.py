#Faça um programa que verifique se tem SILVA no nome ou sobrenome da pessoa
nom = str(input('Qual o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nom.lower()))

