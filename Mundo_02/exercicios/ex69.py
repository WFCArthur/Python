'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.'''
from time import sleep

maiores_18 = 0
homens = 0
mulheres_20 = 0 
cont = 0
while True:
    print('~~'*10)
    print('CADASTRO DE PESSOAS')
    print('~~'*10)

    idade = int(input('Digite a sua idade: '))
    while idade < 1: # sem número negativo.
        idade = int(input('Digite novamente: '))

    sexo = input('Qual o seu sexo: [F/M] ').upper().strip()[0]
    while sexo not in 'FM': # só vai aceitar F ou M.
        sexo = input('Digite novamente: [F/M] ').upper().strip()[0]

    continua = input('Deseja continuar cadastrado: [S/N] ').upper().strip()[0]
    while continua not in 'SN': # Só vai aceitar S ou N.
        continua = input('Digite novamente: [S/N] ').upper().strip()[0]
    
    if idade > 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1

    if continua == 'N':
        print('ENCERRANDO PROGRAMA EM...')
        sleep(0.3)
        print('3')
        sleep(0.9)
        print('2')
        sleep(0.6)
        print('1')
        sleep(0.3)
        break
print('~~'*20)
print(f'{maiores_18} Pessoas com mais de 18 anos.')
print(f'{homens} Homens cadastrados.')
print(f'{mulheres_20} Mulheres com menos de 20 anos.')
print('~~'*20)