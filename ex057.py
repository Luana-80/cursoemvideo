#Desafio057: Faça um programa que leia o sexo de uma pessoa, mas sò aceite M ou F.
# Caso esteja errado, peça a digitaçao novamente atè ter um valor correto.
sexo = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos. Por favor digite o seu sexo [M/F]')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))





