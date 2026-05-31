'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

# Lista principal
lista = list()
# Duas listas de pares e impares.
par = list()
impar = list()

for n in range(0,7):
    num = int(input('Digite um número: '))
    # Fiz a vericação pra saber se é par ou se é impar.
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
# E adicionei as duas listas em uma lista só que é a principal.
lista.append(par)
lista.append(impar)

# Lista exibida em ordem crescente.
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')
