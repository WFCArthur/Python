'''Crie umm programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.

b) A média de idade do grupo. 

c) Uma lista com todas as mulheres.

d) Uma lista com todas as pessoas com idade acima da média.'''


dados = dict()
lista = []
soma = media = 0

# Declarando os dados.
while True:
    dados['nome'] = str(input('Digite o seu nome: ')).capitalize()
    dados['sexo'] = str(input('Qual o seu sexo: [M/F] ')).upper()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('[ERRO], digite novamente!: [M/F] ')).upper()[0]
    dados['idade'] = int(input('Qual a sua idade? '))
    soma += dados['idade']
    continua =  str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continua not in 'SN':
        continua = str(input('[ERRO], digite novamente!: [S/N] ')).upper()[0]
    print('-='*20)
    lista.append(dados.copy())
    if continua == 'N':
        break
# Montando os prints formatados.
media = soma / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) Mulheres encontradas ', end='')
for p in lista:
    if p["sexo"] == 'F':
        print(p["nome"],end=';')
print()
print('D) Lista com pessoas que estão acima da média:') 
for p in lista:
    if p["idade"] > media:
        for k,v in p.items():
            print(f'  {k} = {v}; ', end='')
        print()

print('<<ENCERRADO>>')