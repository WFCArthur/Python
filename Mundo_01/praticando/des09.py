# \033[1;33m \033[m
# Desafio 9 (Jokenpô simples)

# Usuário escolhe: Pedra, Papel ou Tesoura
# Computador escolhe aleatório
# Mostre quem ganhou

from random import randint
from time import sleep
print('====== JOKENPÔ ======')

print('-=-=-=- Escolha uma das opções =-=-=-=-')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

opcao = int(input('Escolha uma opção: '))

if opcao > 2 or opcao < 0:
    print('Opção invalida! TENTE NOVAMENTE.')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(0.50)
print('PÔ')

print('-'*20)
lista = ['Pedra','Papel','Tesoura']
computador = randint(0,2)

print(f'O jogador escolheu {lista[opcao]}')
print(f'O computador escolheu {lista[computador]}.')

print('-='*10)
if opcao == computador:
    print('Deu empate!')
elif opcao == 0 and computador == 2:
    print('Você me venceu! PARABENS.')
elif opcao == 1 and computador == 0:
    print('Você me venceu! PARABENS.')
elif opcao == 2 and computador == 1:
    print('Você me venceu! PARABENS.')
else:
    print('Eu Ganhei! hahaha')
print('-='*10)


