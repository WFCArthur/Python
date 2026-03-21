# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
dinhe = float(input('Quantos reais R$00.00 você tem guardado? R$'))
dolar = dinhe / 5.14

print(f'O valor que você tem na carteira é R${dinhe:.2f} reais e dá para comprar US${dolar:.2f} dolares.')