'''Crie um programa que vai ler vários números e colocar em uma lista.
depois disso, mostre:

a) Quantos números foram digitados.

b) A lista de valores, ordernada de forma decrescente.

c) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continua = input('Deseja continua? [S/N] ').upper()[0]
    while continua not in 'SN':
        continua = input('Digite uma resposta valida: [S/N] ').upper()[0]
    if continua == 'N':
        print('Fim do Programa.')
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
