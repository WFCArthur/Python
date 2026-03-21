# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produ = float(input('Digite o valor atual do produto:'))


con = produ - (produ * 5 / 100)

print(f'O valor digitado foi R${produ:.2f} reais, com 5% de desconto o novo valor ficara ${con:.2f} reais')