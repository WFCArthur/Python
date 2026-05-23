'''Crie um programa que vai ler vários números e colocar em uma lista.
depois disso, crie duas listas externas que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''


lista_principal = list()
lista_par = list()
lista_impar = list()
while True:
    lista_principal.append(int(input('Digite um número: ')))

    continua = input('Deseja continuar? [S/N] ').upper()[0]
    while continua not in 'SN':
        continua = input('[ ERRO ] Opção invalida, Por favor tente novamente: [S/N] ').upper()[0]

    if continua == 'N':
        print('Fim do programa.')
        break

for n in lista_principal:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print('-='*20)
print(f'Lista principal {lista_principal}.')
print(f'Lista que contém só os números pares {lista_par}.')
print(f'Lista que contém só os números ímpares {lista_impar}')
