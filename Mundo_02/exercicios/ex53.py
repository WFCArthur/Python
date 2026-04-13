# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.

# minha solução sem FOR.

# frase = input('Digite uma frase: ').upper()

# frase_sem_espaco = frase.replace(' ', '')

# invertida = frase_sem_espaco[::-1]

# if frase_sem_espaco == invertida:
    # print(f'Temos um Palíndromo. {invertida}')
# else:
    # print(f'Não é um Palíndromo. {invertida}')

# outra solução com FOR.

frase = str(input('Digite uma frase: ')).strip().upper()
pala = frase.split()
junt = ''. join(pala)
inverso = ''
for l in range(len(junt)-1,-1,-1):
    inverso += junt[l]
print(f'O inverso de {junt} é {inverso}.')
if inverso == junt:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é PALÍNDROMO!')