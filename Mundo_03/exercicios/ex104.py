'''Crie um programa que tenha a função input() do python, só que fazendo a validação para aceitar apenas  um valor numérico.
EX: 
n = leiaint('Digite um n')'''

def leiaint():

    while True:

        n = input('Digite um número: ')

        if n.isnumeric():
            return f'\033[32mVocê digitou o número {n}.\033[m'
        else:
            print('\033[31m[ERRO] você não digitou um número.\033[m')

print(leiaint())