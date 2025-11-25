n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1F} e {:.1F} a media do aluno é {:.1F}'.format(n1, n2, media))
if media >= 7:
    print('O aluno està APROVADO!')
elif 7 > media >=5:
    print('O aluno està de RECUPERAçAO!')
else:
    print('O aluno està REPROVADO!')