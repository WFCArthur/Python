# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

 # O programa deverá escrever na tela se o usuário venceu ou perdeu.


 # num = int(input('Ei!! estou pensando em um número tente adivinhar:'))

 # if num == 3:
    # print('Você acertou!!')
 # else:
    # print('Você errou tente novamente!!.')

# outro exemplo usando float!

# num = float(input('Digite um número Float de 1.0 a 10.00 e ve qual eu estou pensando:'))

# if num == 5.0:
    # print('Você acertou!')
# else:
    # print('Você errou!')

# agora com STR!

# nome = str(input('Digite o nome de uma fruta e ve se é mesma que eu estou pensando:'))

# if nome == 'maçã':
    # print('Você acertou!')
# else:
    # print('Você errou!')

# Agora o definitivo 

from random import randint # vai fazer o computador pensar em número.
from time import sleep # vai pensar um pouco antes de dar a resposta.

computa = randint(0,5) # Faz o computador "Pensar"

print('-=-' * 20)
print('Eu estou pensando em número de 0 a 5. tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei?')) # joagador tenta adivinhar.

print('PROCESSANDO...')
sleep(2) # 2s é o tempo que vai demorar para pensar

if jogador == computa:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computa} E não no {jogador}')