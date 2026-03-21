# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

an = float(input('Digite o ângulo que você deseja:'))

sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))

print(f'O ângulo de {an} tem o SENO de {sen:.2f}!')     
print(f'O ângulo de {an} tem o COSSENO de {coss:.2f}!')          
print(f'O ângulo de {an} tem a TANGENTE de {tang:.2f}!')    
