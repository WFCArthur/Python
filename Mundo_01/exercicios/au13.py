# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sala = float(input('Digite o seu salário:'))

aumen = sala + (sala * 15 / 100)

print(f'O salário Digitado foi ${sala:.3f} reais,com 15% de aumento foi para ${aumen:.3f} reais')