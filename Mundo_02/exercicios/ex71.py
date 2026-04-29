'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues.

obs: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.'''



print('='*20)
print('BANCO CENTRAL DE NY')
print('='*20)

valor = int(input('Digite o valor a ser sacado:R$')) # O valor que será sacado.

ced = 100 # Primeira tentativa com a nota de 50.
total = valor # Esse total vai guardar o valor para depois tirar
quant = 0 # Quantidade de notas usadas
while True: # Entra no loop
    if total >= ced: # Verifica se da pra tirar 50 do total.
        total -= ced 
        quant += 1   # Se der ele vai tirar e contar quantas.
    else:
        if quant > 0: # Aqui só vai mostrar se a quantidade for mair do que zero.
            print(f'{quant} notas de R${ced:.2f} reais')
        quant = 0  # Depois vai zerar o contador quando não der mais para tirar, ai ele vai tentar com outras notas.
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else:
            break # Quando não der mais o Loop vai parar.