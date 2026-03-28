# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO

# Média entre 5.0 e 6.9: RECUPERAÇÃO

# Média 7.0 ou superior: APROVADO

print('-=-'*10)
print('PROGRAMA DE CALCULO DE MÉDIA')
print('-=-'*10)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

con = (n1 + n2) / 2

if con < 5.0:
    print(f'A sua nota é {con:.1f}')
    print('Você está REPROVADO!')
elif con == 5.0 and 6.9 or con < 6.9:
    print(f'A sua nota é {con:.1f}')
    print('Você está em RECUPERAÇÃO')
elif con >= 7.0:
    print(f'A sua nota é {con:.1f}')
    print('Você está APROVADO')
else:
    print(f'[ ERRO ] nota {con}')