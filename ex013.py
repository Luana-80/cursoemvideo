#Desafio13: Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
s = float(input('Escreva o seu salàrio: R$ '))
a = s + (s * 15 / 100)
print('Com 15% de aumento, o seu salàrio subiu de R${:.2f} para {:.2f}'. format(s, a))
