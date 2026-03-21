# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o seu salário?'))

if sal > 1250:
    novo = sal + (sal * 10 / 100)
    print(f'Seu novo salário com 10% de aumento foi para R${novo}')
else:
    novo = sal + (sal * 15 / 100)
    print(f'Seu novo salário com 15% de aumento foi para R${novo}')




# aum1 = sal + (sal * 10 / 100) 