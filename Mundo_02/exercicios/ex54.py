# Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

contador_menor = 0
contador_maior = 0

ano_atual = date.today().year

for c in range (1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - ano # mostra a idade

    if idade < 18:
        contador_menor += 1
    else:
        contador_maior += 1

print(f'{contador_menor} são menores e {contador_maior} são maiores.')