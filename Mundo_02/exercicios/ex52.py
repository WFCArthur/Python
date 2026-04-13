# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# minha solução.

# num = int(input('Digite um número: '))

# primo = True
# if num <= 1:
    # print('Não é primo.')
# else:
    # primo = True
# for n in range(2,num):
    # if num % n == 0:
       # primo = False
        #break 
# if primo == False:
    # print('Não é um número primo.')
# else:
    # print('É um número primo.')

# outra solução mais simples.

# para saber se um número é primo ele tem que ser divisivel por 1 e por ele mesmo.

num = int(input('Digite um número: '))

con = 0

for d in range(1,num + 1):
    if num % d == 0:
        print(f'\033[34m', end='')
        con += 1
    else:
        print('\033[31m', end='')
    print(f' {d} ', end='')
print(f'\n\033[37mO número {num} é divisivel {con} vezes')
if con == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele não é PRIMO!')


