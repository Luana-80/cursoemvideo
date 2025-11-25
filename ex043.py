peso = float(input('Qual o seu peso: (KG) '))
altura = float(input('Qual a sua altura: (M) '))
imc = peso / (altura * altura) #ou peso / (altura ** 2)
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Voce està ABAIXO do peso normal. CUIDADO!')
elif imc <= 24.9:
    print('PARABéNS! Voce esta com o peso NORMAL ')
elif imc <=29.9:
    print('Voce esta com SOBREPESO.')
elif imc <=39.9:
    print('Voce esta com OBESIDADE')
else:
    print('Voce esta com OBESIDADE MORBIDA! CUIDADO!!!')