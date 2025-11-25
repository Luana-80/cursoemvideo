#Escreva um programa para aprovar o emprestimo bancario de uma casa. Perguntar valor da casa,.
#o salario do comporador e em quantos anos ele vai pagar. Calcule o valor da prestacao mensal
#sabendo que ela nao deve exceder 30% do salario ou entao o emprestimo sera negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salario do comprador? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
limite = (salario * 30) /100
prestacao = casa / (anos * 12)
if prestacao > limite:
    print('EMPRESTIMO NEGADO! A prestacao de R$ {:.2f} ultrapassa seu limite de 30% ou R$ {:.2f}'.format(prestacao, limite))
else:
    print('PARABENS! O seu limite de gasto é de R$ {:.2f} e a prestacao da sua casa ficarà em R$ {:.2f}'.format(limite, prestacao))

