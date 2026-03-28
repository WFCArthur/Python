# Refaça o Desafio 035 dos triângulos, acrescetando o recurso de mostrar que tipo de traângulo será formado:

# Equilátero: todos os lados iguais.

# Isósceles: dois lados iguais.

# Escaleno: todos os lados diferentes.

# ex 35 / Mundo_01

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas pdem ou não formar um triângulo.

# a + b > c, \quad a + c > b, \quad b + c > a
from time import sleep

print('-=-'*8)
print('DESAFIO DOS TRIÂNGULOS')
print('-=-'*8)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
print('CARREGANDO...')
sleep(2)

print('-'*20)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:

    if r1 == r2 == r3:
        print('Os segmentos podem formar um triângulo Equilátero.')

    elif r1 == r2 or r1 == r3 or r2 == r3 :
        print('Os segmentos podem formar um triângulo Isósceles.')

    elif r1 != r2 != r3 != r1:
        print('Os segmentos podem formar um triângulo Escaleno.') 
else:
    print('Não forma um Triangulo!')
    
print('-'*20)
