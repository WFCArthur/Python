# \033[1;33m \033[m
print('===== \033[1;32mAUMENTO DE SALÁRIO\033[m =====')

sal = float(input('Digite o seu salário: '))

aumen = sal + (sal * 15/100)

print('\033[1;34m-=\033[m'*10)
print(f'O seu salário de R${sal:.2f} reais vai ficar R${aumen:.2f} reais com 15% de aumento!')
print('\033[1;34m-=\033[m'*10)