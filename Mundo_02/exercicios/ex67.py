'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interronpido quando o número solicitado for negativo.'''

from time import sleep
print('=-'*20)
print('DIGITE UM NÚMERO E RECEBA A SUA TABUADA')
print('-='*20)

tab = 10
cont = n = 0

while True:
    num = int(input('Qual tabuada que você quer saber? '))
    cont = 0 
    if num < 0:
        print('Programa Finalizando Em...')
        sleep(0.5)
        print('3')
        sleep(0.8)
        print('2')
        sleep(0.6)
        print('1')
        sleep(0.4)
        print('Programa Finalizado. Volte sempre!')
        break
    print('~~~'*10)
    print('Gerando tabuada...')
    print('~~~'*10)
    sleep(1)
    while cont < tab:
        cont += 1
        r = num * cont
        print(f'{num} x {cont} = {r}')
    print('-='*20)

