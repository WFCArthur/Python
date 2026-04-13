# Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.

# outra maneira usando append()

#lista = []
# peso = float(input('Digite o peso da {}ª: '. format(c)))
    # lista.append(peso)
    # maior = max(lista)
    # menor = min(lista)
# print(f'O maior peso é {maior} e o menor peso é {menor}.')

# variáveis que vão armazenar o maior e o menor peso.

maior = 0 
menor = 0 

for p in range(1,6): # criação do loop. que repete 5 vezes de (1 até 5)
    peso = float(input(f'Digite o peso da {p}ª: ')) # pergunta o peso e repete 5 vezes.

    if p == 1: # verificação e atribuição de peso para as duas variaveis.
        maior = peso # ele vai atribuir o primeiro peso e depois vai verificar se é maior.
        menor = peso # ele vai atribuir o primeiro peso e depois vai verificar se é menor.

    else: # verificação.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
# resultado
print(f'O maior peso foi {maior}kg.')
print(f'O menor peso foi {menor}kg.')
    
    