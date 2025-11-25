#Desafio11: Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua àrea e a qtd de tinta necessaria para pinta-la, sabendo que cada litro de tinta cobre uma area de 2m°
h = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
a = h * l
t = a / 2
print ('A area da parede {:.2f}m x {:.2f}m é de {:.2f}m2. \nVoce deve comprar {:.2f} litros de tinta. '.format(h, l, a, t))

