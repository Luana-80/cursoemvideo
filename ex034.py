#Desafio34: Escreva um programa que pergunte o salario de um funcionario e calcule o valor  do seu
#aumento. para superiores a R$1250 calcule aumento de 10% e para inferiores, o aumento é de 15%
salario = float(input('Qual é o seu salario? R$ '))
if salario > 1250:
    aumento = salario + (salario * 10) / 100
else:
    aumento = salario + (salario * 15) / 100
print('O seu salario apos o aumento sera de R$ {:.2f}'.format(aumento))

