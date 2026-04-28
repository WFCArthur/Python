'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário quer continuar. no final
mostre.

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato.'''

print('=-'*20)
print('MERCADO DO BARÃO')
print('-='*20)

valor_total = 0
produto_mais_1000 = 0
menor = 0
quant = 0
nome_barato = ''

while True:
    nome_do_produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto:R$'))
    quant += 1
    valor_total += preco

    if preco > 1000:
        produto_mais_1000 += 1

    if quant == 1 or preco < menor:
        menor = preco
        nome_barato = nome_do_produto
    continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if continua == 'N':
        print('programa finalizado.')
        break
        
    print('=-'*20)
print(f'O valor total da compra foi R${valor_total:.2f} reais.')
print(f'{produto_mais_1000:.0f} produtos que custam mais de R$1000.00 reais')
print(f'E o produto mais barato é {nome_barato} que custa R${menor:.2f}')