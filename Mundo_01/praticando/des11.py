# \033[1;33m \033[m
# Peça um número
# Mostre a tabuada dele (de 1 a 10)
from time import sleep
print('====== DIGITE UM NÚMERO E DESCUBRA SUA TABUADA ======')

num = int(input('Digite um número: '))

res0 = num * 0
res1 = num * 1
res2 = num * 2
res3 = num * 3
res4 = num * 4
res5 = num * 5
res6 = num * 6
res7 = num * 7
res8 = num * 8
res9 = num * 9
res10 = num * 10
print('GERANDO TABUADA....')
sleep(3)

print('-'*10)
print(f'{num} x 0 = {res0}')
print(f'{num} x 1 = {res1}')
print(f'{num} x 2 = {res2}')
print(f'{num} x 3 = {res3}')
print(f'{num} x 4 = {res4}')
print(f'{num} x 5 = {res5}')
print(f'{num} x 6 = {res6}')
print(f'{num} x 7 = {res7}')
print(f'{num} x 8 = {res8}')
print(f'{num} x 9 = {res9}')
print(f'{num} x 10 = {res10}')
print('-'*10)