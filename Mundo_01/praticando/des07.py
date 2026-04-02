# \033[1;33m \033[m

print('====== BRINCADEIRA DO ÍMPAR OU PAR ======')

num = int(input('Digite um número: '))

res = num % 2

if res == 0:
    print('O número é Par!')
else:
    print('O número é Ímpar!')

