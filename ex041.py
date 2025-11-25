from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'. format(idade))
if idade >25:
    print('Classificaçao: MASTER')
elif 25 > idade > 19:
    print('Classificaçao: SENIOR')
elif 19 > idade > 14:
    print('Classificaçao: JUNIOR')
elif 14 > idade > 9:
    print('Classificaçao: INFANTIL')
else:
    print('Classificaçao: MIRIM')


