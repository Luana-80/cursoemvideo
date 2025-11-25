print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opçao = int(input('Qual é a opçao? '))
if opçao == 1:
    total = preço - (preço * 10) / 100 #calculo do desconto
elif opçao == 2:
    total = preço - (preço * 5) / 100
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra serà parcelada em 2x de R$ {} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20) / 100 #calculo dos juros
    total_parcela = int(input('Em quantas parcelas? '))
    parcela = total / total_parcela
    print('Sua compra serà parcelada em {}x de R${} COM JUROS'.format(total_parcela, parcela))
else:
    total = preço
    print('OPçAO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE! ')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preço, total))



