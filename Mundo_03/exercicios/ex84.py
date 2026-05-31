'''Faça um programa que leia nome e peso de várias pessoas.
Guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.

b) Uma listagem com as pessoas mais pesadas.

c) Uma listagem com as pessoas mais leves.'''


# Declaração de variaveis
dados = list()
princ = list()
cont = 0

# Um loop para perguntar o nome e o peso da pessoa e guardar na variavel dados.
while True:
    dados.append(str(input('Digite o seu Nome: ')).capitalize())
    dados.append(float(input('Digite o seu Peso: ')))
    princ.append(dados[:])
    dados.clear()

    # Pergunta se a pessoa quer continuar.
    continua = str(input('Deseja continuar:[S/N]')).upper()[0]
    while continua not in 'SN':
        continua = str(input('Tente-novamente. deseja continuar? [S/N]')).upper()[0]
    # Se caso não o break para o programa.
    if continua == 'N':
        break

print('-='*20)
print(f'Ao todo foram {len(princ)} pessoas cadastradas.')

for p in princ:
    if cont == 0 :
        peso_maior = p[1]
        peso_menor = p[1]
        cont += 1
    else:
        if p[1] > peso_maior:
            peso_maior = p[1]
        if p[1] < peso_menor:
            peso_menor = p[1]


print(f'E o maior peso foi de {peso_maior}kg. Peso de', end=' ')
for n in princ:
    if n[1] == peso_maior:
        pessoas_pesadas = [n[0]]
        print(pessoas_pesadas, end=' ')
print()

print(f'E o menor peso foi de {peso_menor}kg. peso de',end=' ')
for n in princ:
    if n[1] == peso_menor:
        pessoas_leves = [n[0]]
        print(pessoas_leves,end=' ')