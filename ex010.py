#Desafio10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1.00 = R$ 6.05
din = float(input('Quanto dinheiro tem na sua carteira? R$ '))
d  = din / 5.98
e = din / 6.22
print('Com {:.2f} reais voce pode comprar: \n{:.2f} dolares ou \n{:.2f} euros hoje'. format(din, d, e))
