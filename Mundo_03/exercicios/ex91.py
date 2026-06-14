'''Crie um programa onde 4 jogadores jogem um dado e tenha resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep

jogador = dict()

for joga in range(0,4):
    jogador[f'jogador{joga+1}'] = randint(1,6)
for key,numero in jogador.items():
    print(f'{key} tirou {numero} no dado.')
    sleep(0.7)

print('-='*20)

ordem = sorted(jogador.items(), key=lambda item: item[1], reverse=True)

print(' === RANKING DOS JOGADORES ===')
for pos, (nome,valor) in enumerate(ordem):
    print(f'   {pos+1}º lugar: {nome} com {valor}.')
    sleep(0.7)



