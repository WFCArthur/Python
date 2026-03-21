# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

alu01 = str(input('Primeiro aluno:'))
alu02 = str(input('Segundo aluno:'))
alu03 = str(input('Terceiro aluno:'))
alu04 = str(input('Quarto aluno:'))

lista = [alu01, alu02, alu03, alu04]

res = choice(lista)
print(f'O aluno sorteado foi == !{res}!')

