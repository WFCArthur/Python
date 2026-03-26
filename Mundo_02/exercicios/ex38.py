# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior 

# O segundo valor é maior

# Não existe valor maior, os dois são iguais

num0 = float(input('Digite um Número: '))
num1 = float(input('Digite um Número: '))

if num0 > num1:
    print(f'O primeiro valor é maior {num0}!')
elif num1 > num0:
    print(f'O segundo valor é maior! {num1}')
else:
    print('Não existe valor maior, os dois são iguais!')