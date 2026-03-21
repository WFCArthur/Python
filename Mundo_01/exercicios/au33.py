# faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
n3 = int(input('Terceiro número:'))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print(f'{maior} é maior')
print(f'{menor} é menor')

    