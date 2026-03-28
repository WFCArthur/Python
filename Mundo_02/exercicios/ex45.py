# Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('===== JOKENPÔ =====')

print(' [ 1 ] Pedra')
print(' [ 2 ] Papel')
print(' [ 3 ] Tesoura')

opcao = int(input('Digite uma opcao: '))

if opcao not in [1,2,3]:
    print('Opção invalida! Tente novamente.')
    exit()

print('Jo')
sleep(0.50)
print('Ken')
sleep(0.5)
print('Pô!!')

# Escolha do computador.
lista = ['Pedra','Papel','Tesoura']
computador = random.choice(lista)
print('-='*15)
print(f'Computador escolheu {computador}')

# Transforma a opção do jogador em pedra, papel ou tesoura.
if opcao == 1:
    jogador = 'Pedra'
elif opcao == 2:
    jogador = 'Papel'
elif opcao == 3:
    jogador = 'Tesoura'
print(f'Você escolheu {jogador}')
print('-='*15)

# Lógica do jogo
if computador == jogador:
    print('Deu empate!')
elif (computador == 'Pedra' and jogador == 'Papel') or (computador == 'Papel' and jogador == 'Tesoura') or (computador == 'Tesoura' and jogador == 'Pedra'):
    print('\033[1;33mVocê me venceu! PARABÉNS.\033[m')
else:
    print('\033[1;31mEu te venci!\033[m')
      
     
    


