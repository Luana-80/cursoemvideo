#Desafio19: Faça um prof sortear um dos seus 4 alunos para apagar o quadro. O programa deve ler o nome deles e escrever o nome escolhido.
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))