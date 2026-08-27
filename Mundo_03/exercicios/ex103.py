'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. '''

nome = str(input('Nome: ')).capitalize()
gols = (input('Quantos gols: '))

def ficha(nome='',gols=''):
    if nome == '':
        nome_jogador = 'Desconhecido'
    else:
        nome_jogador = nome
    
    if gols.isnumeric():
        gols_partida = gols
    else:
        gols_partida = 0

    return f'O jogador {nome_jogador} e ele fez {gols_partida} gols na partida.'

print(ficha(nome,gols))



