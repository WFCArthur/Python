# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite um numero: '))
razao = int(input('Digite outro número: '))

d = 1 
termo = primeiro
while d <= 10:
    print(termo,'>', end=' ')
    termo = termo + razao
    d += 1
print('Fim')