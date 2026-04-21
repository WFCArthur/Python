# crie um programa que leia varios números inteiros pelo teclado.
# no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
r = 'S'
soma = quan = maior = menor = 0
while r == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quan += 1
    if quan == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = input('Deseja continuar: [S] [N] ').upper()[0]

media = soma / quan


print(f'A média entre os valores é {media}.')
print(f'O maior é {maior}.')
print(f'O menor é {menor}.')