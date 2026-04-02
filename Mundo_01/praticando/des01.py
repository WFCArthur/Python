from time import sleep
print('===== \033[1;33mAPRESENTAÇÃO\033[m =====')
nome = str(input('Digite seu primeiro nome: '))
print('CARREGANDO...')
sleep(1)

print('-='*10)
print(f'Olá, {nome}! \033[1;37mSeja bem-vindo!\033[m')
print('-='*10)