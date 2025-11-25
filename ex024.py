#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome SANTO
cid = str(input('Em que cidade voce nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')
