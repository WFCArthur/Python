'''Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.

b) A soma dos valores da terceira coluna.

c) O maior valor da segunda linha.'''

matriz = [[],[],[]]

soma_par = soma_terceira_coluna = maior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Digite um número [{linha},{coluna}]: '))
        matriz[linha].append(num)

        if num % 2 == 0:
            soma_par += num

        if coluna == 2:
            soma_terceira_coluna += num

        if linha == 1:

            if coluna == 0:
                maior = num

            elif num > maior:
                maior = num
print('-='*20)
for numero in matriz:
    for coluna in numero:
        print(f'[ {coluna:^4} ]', end='')
    print()

print('-='*20)
print(f'A soma de todos os números pares é {soma_par}.')
print(f'A soma de todos os números da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior}.')