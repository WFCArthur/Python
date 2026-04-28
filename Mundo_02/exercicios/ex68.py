'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitória concecutivas
que ele conquistou no final do jogo.'''
from random import randint

print('=-'*20)
print('VAMO JOGAR PAR OU ÍMPAR')
print('-='*20)

cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    impar_ou_par = int(input('Par ou ímpar? [1/2] '))
    while impar_ou_par != 1 and impar_ou_par != 2:
        impar_ou_par = int(input('tente novamente: apenas [1/2] '))
    computador = randint(0,10)

    if impar_ou_par == 1:
        res = 'Par'
    elif impar_ou_par == 2:
        res = 'Impar'

    som = jogador + computador

    if som % 2 == 0:
        com = 'Par'
    else:
        com = 'Impar'

    print('--'*20)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {som} DEU {com}')
    print('--'*20)

    if res == com:
        cont += 1
    else:
        print(f'VOCÊ PERDEU!')
        print('-='*20)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break