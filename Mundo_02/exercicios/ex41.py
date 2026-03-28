# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo coma a idade:

# Até 9 anos : MIRIM
# Até 14 anos : INFANTIL
# Até 19 anos : JUNIOR
# Até 25 anos :SÊNIOR
# Acima: MASTER
from time import sleep
from datetime import date

print('-=-'*7)
print('CATEGORIAS DE NATAÇÃO')
print('-=-'*7)

ano_atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = ano_atual - ano

print('CARREGANDO....')
sleep(2)

print('-'*15)
if idade <= 9:
    print(f'O atleta tem {idade} anos')
    print('Classificação: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos')
    print('Classificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos')
    print('Classificação: JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos')
    print('Classificação: SÊNIOR')
elif idade > 25:
    print(f'O atleta tem {idade} anos')
    print('Classificação: MASTER')
else:
    print('[ ERRO ]')
print('-'*15)