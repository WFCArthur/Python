'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatação correta.'''

#    0 1 2
# 0 [][][]
# 1 [][][]
# 2 [][][]

# Primreira etapa

matriz = [
            [],
            [],
            []
        ]
for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite um número [{l},{c}]:'))
        matriz[l].append(num)
print('-='*20)
for n in matriz:
    for c in n:
        print(f'[ {c:^4} ]',end='')
    print()