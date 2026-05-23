'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordernada na tela.'''


lista = []
for c in range(0,5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        achou = False
        for pos,e in enumerate(lista):
            if e > num:
                lista.insert(pos,num)
                print(f'Adicionado na posição {pos} da lista... ')
                achou = True
                break
        if achou == False:
            lista.append(num)
print(lista)