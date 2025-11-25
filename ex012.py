#Desafio12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Preço do produto: R$ '))
d = (p * 50) / 100
np = p - d
#modo alternativo: novo = preço - (preço * 5 / 100)
print('O produto de R$ {:.1f} custarà R${:.1f} com 50% de desconto'.format(p, np))
