# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Digite um ano e descubra se ele é BISSEXTO, se você digitar 0 ele vai contar como ano atual:'))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'Ano {ano} é Bissexto!')
else:
    print(f'Ano {ano} não é BISSEXTO!')