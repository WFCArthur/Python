'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um Boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente'''

geral = list()

while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))

    res = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while res not in 'SN':
        res = str(input('Tente-novamente. Deseja continuar? [S/N] ')).upper()[0]

    geral.append([nome,[n1,n2]])

    if res == 'N':
        break

print('-='*25)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":<7}')
print('-'*25)
for pos, n in enumerate(geral):
    media = (n[1][0] + n[1][1]) / 2
    print(f'{pos:<5}{n[0]:<15}{media:<7.1f}')


while True:
    opçao = int(input('Mostra a nota de qual aluno? (999 Interrompe): '))
    print('--'*30)
    if opçao == 999:
        break
    if 0<= opçao < len(geral):
        print(f'Notas de {geral[opçao][0]} são {geral[opçao][1]}')
    else:
        print('[ERRO] O aluno não existe!')
    
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')