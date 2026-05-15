'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos_valor = ('Lápis', 1.75,'Borracha', 2.00,'Caderno', 15.90,'Estojo', 25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas', 22.30,'Livro',34.90)

print('-'*40)
print('{:^40}'. format('LISTAGEM DE PREÇO'))
print('-'*40)

for produto in range(0, len(produtos_valor)):
    if produto % 2 == 0:
        print(f'{produtos_valor[produto]:.<30}R$ {produtos_valor[produto+1]:>7.2f}')
print('-'*40)