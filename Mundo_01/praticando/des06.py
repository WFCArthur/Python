# \033[1;33m \033[m
from datetime import date
print('\033[1;32m====== ALISTAMENTO MILITAR ======\033[m')

ano = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano

print('\033[1;34m-=\033[m'*10)
if idade == 18:
    print(f'Você nasceu em {ano}, tem {idade} anos.')
    print('Pode se alistar IMEDIATAMENTE!')
elif idade > 18:
    tempo_que_passou = ano + 18
    print(f'Você nasceu em {ano}, tem {idade} anos.')
    print('Já passou o tempo de se alistar!')
    print(f'Deveria ter se alistado em {tempo_que_passou}!')
elif idade <= 17 :
    tempo = ano + 18
    falta = tempo - ano_atual
    tempo_exato = ano_atual + falta
    print(f'Você nasceu em {ano}, tem {idade} anos em {ano_atual}.')
    print(f'Ainda não pode se alistar!')
    print(f'Só daqui {falta} anos, em {tempo_exato}!')

print('\033[1;34m-=\033[m'*10)

