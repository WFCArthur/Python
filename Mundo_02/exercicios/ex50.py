# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dequeles que forem pares. se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range(1,7):
    num = int(input(f'Digite o {n}ª valor: '))

    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Você informou {cont} números pares e a soma deles é {soma}')


