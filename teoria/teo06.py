# Cores no terminal
from time import sleep

print('-' * 25)
print('\033[1;34;47m CLASSIFICAÇÃO DE IDADE! \033[m')
print('-' * 25)
idade = int(input('\033[1;33m Digite a sua IDADE:\033[m'))
print('-=-' * 7)
print(f'\033[1;37m A IDADE DIGITADA {idade}\033[m')
print('-=-' * 7)
print('PROCESSANDO...')
sleep(2)

if idade >= 18:
    print(f'\033[1;34m A sua idade é {idade}, você já pode ser preso!\033[m')
else:
    print(f'\033[1;32m A sua idade é {idade}, você é menor de idade!\033[m')