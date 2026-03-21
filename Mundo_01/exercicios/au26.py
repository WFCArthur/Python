# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "a".

# Em que posião ela aparece a primeira vez.

# Em que posição ela aparece a última vez.

nome = str(input('Digite o seu nome:')).upper().strip()

quant = nome.count('A')
prim = nome.find('A') + 1
ult = nome.rfind('A') + 1

print(f'A letra "A" aparece {quant} vezes')
print(f'E ela aparece pela primeira vez na posição {prim}')
print(f'E ela aparece a ultima vez na posição {ult}')
