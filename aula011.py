#Cores no Terminal
nome = 'Luana'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))

a = 3
b = 5
print('Os valores sao \033[36m{}\033[m e \033[31m{}'.format(a, b))
