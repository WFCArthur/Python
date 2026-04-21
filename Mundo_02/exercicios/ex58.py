# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=' * 20)

computador = randint(0, 10)
tent = 0

jogador = int(input('Digite um número de 0 a 10 e veja se é o que eu estou pensando: '))

while jogador != computador:
    tent = tent + 1
    print('CARREGANDO...')
    sleep(0.8)
    print('Você errou! Tente novamente...')
    if computador > jogador:
        print(f'Mais que {jogador}')
    else:
        print(f'Menos que {jogador}')
    jogador = int(input('Tente novamente: '))
print('=' * 20)

print('Você acertou! Meus parabéns.')
print(f'Você precisou de {tent} tentativas para acertar!')
    
