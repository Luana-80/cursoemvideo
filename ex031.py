#Desafio31: Desenvolva um programa que pergunte a distancia da viagem em km. Calcule o preço da passagem
#cobrando R$ 0.50 por km para viagens de ate 200km e 0.45 para mais longas.
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {} km'.format(distancia))

'''if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A sua passagem vai custar R$ {:.2f}'.format(preço))
