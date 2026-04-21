# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5 ; = 5x4x3x2x1 = 120

n = int(input('Digite um número: '))
num = n
f = 1
print(f'Calculando {n}! = ', end='')
while n > 0:
    print(f'{n}',end=' ')
    f *= n
    n -= 1

    if n > 0:
        print('x ', end='')
print(f'= {f}')

