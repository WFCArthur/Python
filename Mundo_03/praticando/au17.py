#lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
# Troca o lanche por outro
#lanche[3] = 'Picole'
# Adiciona outros lanches
#lanche.append('Cookie')
# Inseri um lanche na posição que você quer
#lanche.insert(0,'Cachorro-Quente')
# Os dois você consegue deletar um item da lista
#del lanche[3]
# Colocando desse jeito ele elimina o ultimo item da lista.
#lanche.pop(3)

#if 'Pizza' in lanche:
#    lanche.remove('Pizza')
#print(lanche)

#valores = list(range(4,11))
#valores = [8,2,5,4,9,3,0]
#valores.sort()
#valores.sort(reverse=True)
#print(len(valores))
#print(valores)

#valores = []

#for c in range(0,5):
#    val = int(input('Digite um número: '))
#    valores.append(val)

#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista.')

# Uma ligação

'''a = [2,3,4,7]
b = a
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

# Essa é uma cópia
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

