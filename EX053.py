#Crie programa que leia uma frase qualquer e diga se ela è um PALINDROMO desconsiderando
# espaços. ex. APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper() #remove espaços e faz maiusculas
palavras = frase.split() #divide a frase em palavras
junto = ''.join(palavras) #junta todas as palavras sem espaços
inverso = '' #variavel que armazenarà o inverso

for letra in range(len(junto) -1, -1, -1): #percorre a string de tras pra frente
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto: #se a string invertida for igual a original serà um palindromo
    print('Temos um palindromo')
else:
    print('A frase digitada nao é um palindromo')