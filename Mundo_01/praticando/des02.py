from time import sleep
print('\033[1;32m++++++ SOMA ++++++\033[m')

primeiro_numero = float(input('Digite um número: '))
segundo_numero = float(input('Digite outro número: '))
print('CARREGANDO...')
sleep(1)

soma = primeiro_numero + segundo_numero

print('\033[1;34m-=\033[m'*10)
print(f'\033[1;37mAs soma entre {primeiro_numero} e {segundo_numero} é {soma}!\033[m')
print('\033[1;34m-=\033[m'*10)