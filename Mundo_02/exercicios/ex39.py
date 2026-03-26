# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.

# Se é a hora de se alistar.

# se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
print('-=-'*13)
print('quantos anos você vai fazer esse ano?')
print('-=-'*13)

idade = int(input('Digite a sua idade: '))

print('CARREGANDO....')
sleep(2)

ano = 2026 - idade

if idade <= 17:
    print(f'O ano que você nasceu é {ano}')
    print('Você ainda não pode se alistar!')
    print(f'Por que você não tem idade suficiente! {idade} anos')
elif idade == 18:
    print(f'O ano que você nasceu é {ano}')
    print(f'Esse ano você faz {idade} anos, você já pode se alistar!')
elif idade > 19:
    print(f'O ano que você nasceu é {ano}')
    print(f'Já passou do tempo de se alistar! Pois você já tem {idade} anos')
else:
    print('[ERRO]')

print('-'*20)


