'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''


lista = []
while True:

    num = int(input('Digite um número: '))

    if num in lista:
        print('Esse número já está na lista.')
    else:
        print('Número cadastrado com sucesso...')
        lista.append(num)

    continua = input('Deseja continuar? [S/N] ').upper()[0]
    while continua not in 'NS':
        continua = input('Tente-novamente, deseja continuar? [S/N] ').upper()[0]
    
    if continua == 'N':
        break
lista.sort()
print('=-'*20)
print(f'Números cadastrados => {lista}')
