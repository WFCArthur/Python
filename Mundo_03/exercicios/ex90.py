'''Faça um progrma que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
Mostre o conteúdo da estrutura na tela.'''

dado = dict()

dado['nome'] = str(input('Digite o seu Nome: ')).capitalize()
dado['media'] = float(input(f'Média de {dado["nome"]}: '))

if dado['media'] >= 7:
    dado['situação'] = 'APROVADO'
elif 5 <= dado['media'] < 7:
    dado['situação'] = 'RECUPERAÇÃO'
else:
    dado['situação'] = 'REPROVADO'

print('-='*20)
for key,n in dado.items():
    print(f' - {key} é Igual {n}.')
