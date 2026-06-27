'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:inicio,fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da funçaõ criada:
A)De 1 até 10, de 1 em 1.
B)De 10 até 0, de 2 em 2.
C)Uma contagem personalizada.
'''

from time import sleep
def contador(inicio,fim,passo):

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f'Um contador que vai de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
    print('-='*20)


contador(1,10,1)
contador(10,0,2)

print('Agora é a sua vez de personalizar a contagem!')

inc = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
print('-='*20)

contador(inc,fi,pas)


