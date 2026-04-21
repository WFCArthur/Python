# Crie um programa que leia vários números inteiros pelo teclado.
# O progrma só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag).
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número ou [999] para parar: '))
    if num != 999:
        quan += 1
        soma += num 
print('='*20)
print(f'Ao todo {quan} números foram digitados.')
print(f'A soma entre eles é {soma}.')
print('='*20)
