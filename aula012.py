nome = str(input('Qual é seu nome? '))
if nome == 'Tutacanomeupau':
    print('\033[31mIndecente\033[m! Escolha outro nome! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José' or nome == 'Joao Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Nelson Stella Rafaela':
    print('Que nome bonito!')
elif nome in 'Beatrice Ana Julia Natalia Vefago':
    print('Que nome feio...')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

