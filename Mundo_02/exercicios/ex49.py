# Refaça o desafio 009, mostrando a tabuada de um número que o usúario escolher, só que agora utilizando um laço for.
print('====== TABUADA =======')
num = int(input('Digite um número: '))

for i in range(1,11):
    res = i * num
    print(f'{num} x {i} = {res}')
