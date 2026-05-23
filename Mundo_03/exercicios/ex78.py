'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

# Lista.
lista = []

# Pede um número e adiciona na lista.
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {n}: ')))
    maior = max(lista)
    menor = min(lista)

# Mostra a lista.
print('-='*30)
print(f'Você digitou os valores {lista}')

# Mostra o maior e quais foram as suas posições.
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos,n in enumerate(lista):
    if n == maior:
        print(f'{pos}... ',end='')
print()

# Mostra o menor e quais foram as suas posições.
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos,n in enumerate(lista):
    if n == menor:
        print(f'{pos}... ', end='')

print()
# Fim do programa