'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro indique o número a calcular e o outro chamado show,
que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


num = int(input('Digite um valor: '))

def fatorial(num,show=True):
    res = 1
    for i in range(num,0,-1):
        res *= i
        if show:
            print(f'{i}', end=' ')
            if i == 1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    return res

print(fatorial(num))


