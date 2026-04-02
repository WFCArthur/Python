# \033[1;33m \033[m
# Peça um valor em reais
# Converta para dólares (use valor fixo, tipo 5.00)
from time import sleep
print('====== BANCO DO DOLAR ======')

dinheiro = float(input('Digite o valor que você tem no banco: R$ '))
dolar = dinheiro / 5.16
print('CARREGANDO...')
sleep(2)

print('-='*20)
print(f'O valor que você tem no banco é R${dinheiro:.2f} reais.')
print(f'Com esse dinheiro você consegue comprar US${dolar:.2f} dolares. ')
print('-='*20)