'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

num = ()
for i in range(0,5):
    com = randint(1,10)
    num = num + (com,)

maior = max(num)
menor = min(num)

print(f'Os números são {num}')
print(f'O maior {maior}')
print(f'O menor é {menor}')