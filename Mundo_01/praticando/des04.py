# \033[1;33m \033[m
from time import sleep
print('===== \033[1;33mNOTA DA PROVA\033[m =====')

n1 = float(input('Digite uma nota: '))
print('CARREGANDO...')
sleep(1)
print('\033[1;34m-=\033[m'*10)
if n1 >= 6:
    print(f'Você tirou {n1}, situação: APROVADO! PARABÉNS.')
else:
    print(f'Você tirou {n1}, situação: REPROVADO!')
print('\033[1;34m-=\033[m'*10)