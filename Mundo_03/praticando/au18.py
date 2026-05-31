'''teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]

for p in galera:
    print(f'O {p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')).capitalize())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

'''for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaio += 1
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade.')
print('-='*30)
print(f'No total foi {totmaio} pessoas maiores de idade.')
print(f'No total foi {totmen} pessoas menores de idade.')'''