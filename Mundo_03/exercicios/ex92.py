'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date

dado = dict()

# Nome
dado['nome'] = str(input('Digite o seu nome: ')).capitalize()
# Idade
ano = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
dado['idade'] = ano_atual - ano
# Carteira de trabalho
dado['ctps'] = int(input('Digite a sua carteira de trabalho: (0 não tem) '))

if dado['ctps'] != 0:
    dado['contratação'] = int(input('Digite o ano da contratação: '))
    dado['salario'] = float(input('Digite o salário: R$ '))
    
    dado['aposentadoria'] = dado['idade'] + ((dado['contratação'] + 35) - ano_atual)

print('-='*20)
for key,d in dado.items():
    print(f' -- {key} tem o valor {d}')

