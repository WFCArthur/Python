# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para Binário
# 2 para Octal
# 3 para Hexadecimal
from time import sleep

print('-=-'*15)
print('\033[1;35m CONVESOR DE BASES (''Binário, Octal, Hexadecimal''\033[m)')
print('-=-'*15)

num = int(input('Digite um Número para converte: '))

print('-'*26)
print('Digite: 1 para Binário')
print('Digite: 2 para Octal')
print('Digite: 3 para Hexadecimal')
print('-'*26)

convert = int(input('Qual seria a sua opção? '))


if convert == 1:
    
    bina = (bin(num)[2:])
    print(f'A opção escolhida foi {convert}')
    print('CONVERTENDO.....')
    sleep(2)
    print(f'Convertendo a Base para Binário ficará "{bina}"')

elif convert == 2:
    octal = (oct(num)[2:])
    print(f'A opção escolhida foi {convert}')
    print('CONVERTENDO.....')
    sleep(2)
    print(f'Convertendo a Base para Octal ficará "{octal}"')
elif convert == 3:
    hexad = (hex(num)[2:])
    print(f'A opção escolhida foi {convert}')
    print('CONVERTENDO.....')
    sleep(2)
    print(f'Convertendo a Base para Hexadecimal ficará "{hexad}"')
else:
    print('Não deu certo!')

