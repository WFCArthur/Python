# Crie um programa que leia dois valores e mostre um menu na tela:

#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa

# Seu programma deverá realizar a operação solicitada em cada caso.
'''n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
op = 0
while op != 5 :
    print('='*20)
    print('ESCOLHA UMA OPÇÃO')
    print('='*20)

    print('[1] Somar.')
    print('[2] Multiplicar.')
    print('[3] Maior.')
    print('[4] Novos números.')
    print('[5] Sair do programa.')

    op = int(input('Digite a sua opção: '))
    print('='*20)
    if op == 1:
        res = n1 + n2
        print(f'A somatória entre {n1} e {n2} é {res}.')
        print('-='*15)
    elif op == 2:
        res = n1 * n2
        print(f'Multiplicando {n1} por {n2} o resultado é {res}')
        print('-='*15)
    elif op == 3:
        if n1 > n2:
            print(f'O primeiro valor {n1} é maior.')
            print('-='*15)
        elif n2 > n1:
            print(f'O segundo valor {n2} é maior.')
            print('-='*15)
        else:
            print('Os dois valores são iguais!')
            print('-='*15)
    elif op == 4:
        n1 = int(input('Digite outro valor: '))
        n2 = int(input('Digite outro valor: '))
    elif op not in [1,2,3,4,5]:
        print('Opção invalida!')
    elif op == 5:
        print('='*20)
        print('Programa Finalizado.')
        print('='*20)'''

# Pedi ao chatgpt para deixar mais bonito usando cores.
# \033[32m São códigos ANSI usados para colorir texto no terminal.
from time import sleep
n1 = int(input('\033[36mDigite um valor: \033[m'))
n2 = int(input('\033[36mDigite outro valor: \033[m'))
op = 0
while op != 5 :
    print('\033[34m' + '='*20)
    print('ESCOLHA UMA OPÇÃO')
    print('='*20 + '\033[m')
    print('''[1] Somar.\n[2] Multiplicar.\n[3] Maior.\n[4] Novos números.\n[5] Sair do programa.''')

    op = int(input('Digite a sua opção: '))
    print('='*20)

    if op == 1:
        res = n1 + n2
        print(f'\033[32m A soma entre{n1} + {n2} = {res}.\033[m')
        print('-='*15)

    elif op == 2:
        res = n1 * n2
        print(f'\033[32m O resultado entre {n1} x {n2} = {res}\033[m')
        print('-='*15)

    elif op == 3:
        if n1 > n2:
            print(f'\033[32mEntre {n1} e {n2} o {n1} é maior.\033[m')
            print('-='*15)
        else:
            print(f'\033[32mEntre {n1} e {n2} o {n2} é maior.\033[m')
            print('-='*15)
        if n1 == n2:
            print('\033[33mOs dois valores são iguais!\033[m')
            print('-='*15)

    elif op == 4:
        n1 = int(input('\033[36mDigite outro valor: \033[m'))
        n2 = int(input('\033[36mDigite outro valor: \033[m'))

    elif op not in [1,2,3,4,5]:
        print('\033[31mOpção invalida!\033[m')

print('Finalizando programa...')
sleep(1)

print('\033[31m' + '='*20)
print('Programa Finalizado. Volte sempre!')
print('='*20 + '\033[m')

