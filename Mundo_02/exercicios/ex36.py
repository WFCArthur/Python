# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
print('-=-' * 9)
print('\033[1;33m PERMISSÃO PARA EMPRESTIMO\033[m')
print('-=-' * 9)

valor_da_casa = float(input('Qual o valor da casa? '))
salario_do_comprador = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos para pagar? '))

print('\033[1;31m CALCULANDO...\033[m')
sleep(2)

meses = anos * 12
prestacao = valor_da_casa / meses
limite = salario_do_comprador * 0.30


if prestacao <= limite:
    print(f'para pagar uma casa de R${valor_da_casa:.2f} reais, em {anos} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo APROVADO ✅')
else:
    print(f'para pagar uma casa de R${valor_da_casa:.2f} reais, em {anos} anos a prestação será de R${prestacao:.2f}')
    print(f'Empréstimo NEGADO ❌')

print('-=-' * 9)
print('FIM DO PROGRAMA!')
print('-=-' * 9)

 
