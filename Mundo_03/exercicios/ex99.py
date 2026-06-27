'''
Faça um programa que tenha uma função chamada maior(),que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(*num):
    tot = mai = 0
    print('Analizando os valores passados...')
    for n in num:
        print(n,end=' ',flush=True)
        tot += 1
        sleep(0.2)
        if n > mai:
            mai = n
    print(f'Foram informados {tot} valores ao todo.')
    print(f'E o maior valor informado foi {mai}.')
    print('-='*30)



maior(1,4,5,3,7,9,10)
maior(7,2,4,5,1)
maior(2,7,1,4,0,4,3)
maior(6,4,3)
maior(10,3,5,7,6,56,8,12,)
maior()
