# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

alu01 = str(input('Primeiro aluno:'))
alu02 = str(input('Segundo aluno:'))
alu03 = str(input('Terceiro aluno:'))
alu04 = str(input('quarto aluno:'))

lista = [alu01,alu02,alu03,alu04]

shuffle(lista)
print(f'A Ordem será essa {lista}')
