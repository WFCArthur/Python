# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# Á vista dinheiro/cheque: 10% de desconto.
# Á vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

print('======= CAIXA =======')

preco = float(input('Qual foi o valor total das compras: R$ '))

print('FORMAS DE PAGAMENTO')

print(' [ 1 ] Á vista no dinheiro ou cheque: 10% de desconto.')
print(' [ 2 ] Á vista no cartão: 5% de desconto.')
print(' [ 3 ] Em até 2x no cartão: preço normal.')
print(' [ 4 ] 3x ou mais no cartão: 20% de juros')

opcao = int(input('Qual a opção? '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco 
    parcela = preco / 2
    print(f'Sua compra parcelada em 2x de {parcela:.2f} reais SEM JUROS')
elif opcao == 4:
    parcela_para_pagar = int(input('Quantas parcelas? '))
    total = preco + (preco * 20/100)
    parcela = total / parcela_para_pagar  
    print(f'Sua compra parcelada em {parcela_para_pagar}x de R${parcela:.2f} reais COM JUROS')
else:
    total = preco
    print('Opção INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preco:.2f} reais, vai custar R${total:.2f} reais no final.')