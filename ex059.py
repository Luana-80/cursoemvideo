#Crie um programa que leia dois valores e mostre um menu na tela: [1]somar [2]multiplicar
#[3]maior [4]novos numeros [5]sair do programa. Seu programa devera realizar a operacao
#solicitada em cada caso.
import time
n1 = int(input('Digite o primeiro n°: '))
n2 = int(input('Digite o segundo n°: '))
opçao = 0
while opçao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos n°s
    [5] sair do programa''')
    opçao = int(input('>>>>>Qual é a sua opçao? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'. format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor ée {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os n°s novamente')
        n1 = int(input('Digite o primeiro n°: '))
        n2 = int(input('Digite o segundo n°: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opçao invalida. Tente novemente')
    print('=-=' * 10)
    time.sleep(2)
print('Fim do programa! Volte sempre!')

