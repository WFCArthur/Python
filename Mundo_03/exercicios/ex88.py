'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

print('-='*20)
print('{:^40}'.format('MEGA SENA'))
print('-='*20)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

total = list()

lista = list()
for palpites in range(0,jogos):
    while len(lista) < 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            lista.sort()
    total.append(lista[:])
    lista.clear()
    
print(F'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
for posicao,jogo in enumerate(total):
    print(f'Jogo {posicao+1}: {jogo}')
    sleep(0.6)
print('-='*5,end=' ')
print('< BOA SORTE! >', end=' ')
print('-='*5)
