#Desafio4: Dissecando uma variàvel

a = input('Digite algo: ')

# Exibe o tipo primitivo
print('O tipo primitivo desse valor é', type(a))

# Verifica se contém apenas espaços
print('Só tem espaços?', a.isspace())

# Verifica se é um número (inteiro)
print('É um número?', a.isnumeric())

# Verifica se é alfanumérico (letras e números)
print('É alfanumérico?', a.isalnum())

# Verifica se está em caixa alta
print('Está em caixa alta?', a.isupper())

# Verifica se está em letras minusculas
print('Està em letras minusculas?' ,a.islower())

# Tentativa de verificar se é um número, incluindo decimais
try:
    float_a = float(a)  # Tenta converter para float
    print('É um número (float)?', True)
except ValueError:
    print('É um número (float)?', False)
