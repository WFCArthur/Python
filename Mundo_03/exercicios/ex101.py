'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''
from datetime import date

print('-'*30)

ano = int(input('Em que ano você nasceu? '))

def voto(ano_de_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_de_nascimento

    if idade < 16:
        resposta = 'Não Vota.'
    elif idade == 16 or idade == 17:
        resposta = 'Voto Opcional.'
    elif idade >=18 and idade <= 69:
        resposta = 'Voto Obrigatório.'
    elif idade >= 70:
        resposta = 'Voto Opcional.'

    res = f'Com {idade} Anos: {resposta}'

    return res

print(voto(ano))