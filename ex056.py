#Faça um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
#a mèdia de idade do grupo, qual o nome do homem mais velho, qtas mulheres tem menos de 20a

soma_idades = 0  # Soma das idades para calcular a média
total_pessoas = 4  # Número total de pessoas
homem_mais_velho = 0  # Idade do homem mais velho
nome_homem_mais_velho = ''  # Nome do homem mais velho
mulheres_menos_20 = 0  # Contador de mulheres com menos de 20 anos

for c in range(1, total_pessoas + 1):
    print(f'==========={c}ª PESSOA===========')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').strip().upper()  # Converter para maiúsculas e remover espaços extras

    soma_idades += idade  # Soma para calcular a média

    # Verifica se é um homem e se ele é o mais velho até agora
    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Conta quantas mulheres têm menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calcula a média das idades
media_idades = soma_idades / total_pessoas

# Exibe os resultados
print(f'\nA média de idade do grupo é: {media_idades:.2f} anos')

if nome_homem_mais_velho:
    print(f'O homem mais velho é {nome_homem_mais_velho} e tem {homem_mais_velho} anos.')
else:
    print('Não foi inserido nenhum homem no grupo.')

print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_20}')
