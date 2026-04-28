'''Crie um programaque leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o vaolor 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)'''

cont = soma = 0
while True:
    n = int(input('Digite um número ou [999] para finalizar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'No total foi digitado {cont} números e somando tudo ficou {soma}.')
