# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite um numero: '))
razao = int(input('Digite outro número: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(termo,'>', end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    print('=-'*20)

    mais = int(input('Quantos termos você quer a mais? [0] para parar: '))

print(f'Programa Finalizado com {total} termos mostrados.')