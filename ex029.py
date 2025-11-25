#Desafio29_ crie um programa que pergunte a velocidade do carro.
# Se estiver acima de 80km/h, mostre msg de que foi multado. A multa vai custar 7 reais cada km acima.

velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade >80: #condiçao simples pq so usou o if
    print('MULTADO! Voce excedeu o limite que è de 80 km/h.')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')


