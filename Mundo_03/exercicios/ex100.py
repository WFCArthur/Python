'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPa(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior''' 

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:',end=' ')
    for i in range(0,5):
        computer = randint(1,10)
        numeros.append(computer)
        print(computer,end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPa(lista):
    soma_dos_pares = 0
    for n in numeros:
        if n % 2 == 0:
            soma_dos_pares += n
    print(f'Somando os valores pares de {numeros}, temos {soma_dos_pares}.')

numeros = list()
sorteia(numeros)
somaPa(numeros)


