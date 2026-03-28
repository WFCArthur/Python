# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.

# Se é a hora de se alistar.

# se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
print('-=-'*8)
print('PROGRAMA DE ALISTAMENTO')
print('-=-'*8)

ano = int(input('Ano de nascimento: '))

print('-'*20)
print('[1] para masculino')
print('[2] Para feminino')
print('-'*20)

genero = int(input('Qual o seu gênero: '))

ano_atual = date.today().year

print('CARREGANDO...')
sleep(2)

print('-'*20)
idade = ano_atual - ano

if genero == 1:
    if idade < 18:
        tempo_que_falta = 18 - idade
        ano_alistamento = ano_atual + tempo_que_falta

        print('Você ainda não pode se alistar.')
        print(f'Pois faltam {tempo_que_falta} anos e você tem {idade} anos.')
        print(f'Você vai se alistar em {ano_alistamento}.')

    elif idade == 18:

        print(f'você já pode se alistar!')

    else:
        tempo_que_passou = idade - 18
        ano_alistamento = ano_atual - tempo_que_passou

        print(f'Já passou do tempo de se alistar.')
        print(f'Você deveria ter se alistado em {ano_alistamento}.')
        print(f'Isso foi há {tempo_que_passou} anos.')
else:
   print(f'Você não precisa se alistar.')

print('-'*20)


