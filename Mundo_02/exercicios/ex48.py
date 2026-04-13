# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# multiplo de 3 é num % 3 == 0 e impar é num % 2 != 0.
num = []
cont = 0
for n in range(1,501,2):
    if n % 3 == 0:
        num.append(n)
        cont += 1
soma = sum(num)
print(f'A soma de todos os {cont} valores de 1 até 500, que são multiplos de 3 e que são impar é {soma}')