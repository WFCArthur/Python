# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da Hipotenusa.
# import math

# cao = float(input('Comprimento do cateto oposto:'))
# cad = float(input('Comprimento do cateto adjacente:'))

# som1 = math.pow(cao, 2)
# som2 = math.pow(cad, 2)

# som3 = som1 + som2

# res = math.sqrt(som3)

# print(f'A hipotenusa vai medir {res:.2f}!')

from math import hypot

cao = float(input('Comprimento do cateto oposto:'))
cad = float(input('Comprimento do cateto adjacente:'))
res = hypot(cao, cad)

print(f'A hipotenusa vai medir {res:.2f}!')

# dois exemplos de como fazer!!
