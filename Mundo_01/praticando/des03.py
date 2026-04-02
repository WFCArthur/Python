# \033[1;33m \033[m
from time import sleep

print('===== \033[1;33mDOBRO, TRIPLO E A RAIZ QUADRADA\033[m =====')

numero = float(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print('CARREGANDO...')
sleep(1)

print('\033[1;34m-=\033[m'*10)
print(f'O dobro de {numero} é {dobro}!')
print(f'O triplo de {numero} é {triplo}!')
print(f'A raiz de {numero} é {raiz:.2f}!')
print('\033[1;34m-=\033[m'*10)
