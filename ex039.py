#Desafio39: Faça um programa que leia o ano de nasc de um jovem e informe de acordo com a
# idade: se ainda vai se alistar, se é hora de se alistar, se ja passou do tempo do alistamento,
# qto tempo falta ou se ja passou do prazo.

from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano do seu nascimento: '))

idade = ano_atual - ano_nasc
idade_alistamento = 18
diferença = idade - idade_alistamento

if idade < idade_alistamento:
    print('Voce tem {} anos. Ainda faltam {} anos para o alistamento'.format(idade, diferença))
    print('Seu alistamento serà em {}'.format(ano_nasc + 18))
elif idade == idade_alistamento:
    print('Voce tem {} anos, é a hora de se alistar!')
else:
    print('Voce tem {} anos. Jà passaram {} anos do prazo do alistamento.'.format(idade, diferença))
    print('Seu alistamento foi em {}'.format(ano_nasc + 18))





