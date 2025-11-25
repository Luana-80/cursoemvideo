#Desafio15: Aluguel de Carros - escreva um programa que pergunte a qtd de km percorridos por um carro
#alugado e a qtd de dias pelos quais ele foi alugado. Calcule o preco a pagar sabendo que o carro custa R$60.00
#por dia e R$ 0.15 por km rodado.
d = int(input('Quantos dias de aluguel?: '))
km = float(input('Quantos km rodados?: '))
v = (d * 90) + (km * 0.30)
print('Para {} dias e {:.2f} km rodados, voce deve pagar R$ {:.2f}'.format(d, km, v))
