# Esse é um desafio proposto pelo ChatGPT, onde consigo mostrar tudo o que aprendi no Mundo 1 do Guanabara.

# Esse projeto usa cores no terminal

# Também utiliza uma biblioteca de tempo para dar a impressão de que o programa realmente está gerando o relatório.

# Também possui condições que verificam algumas situações, como calcular o IMC e verificar a idade da pessoa.

from time import sleep
print('===== SISTEMA DE ANÁLISE DE DADOS =====')

nome = str(input('\033[1;33mDigite o seu nome: \033[m'))
idade = int(input('\033[1;33mDigite a sua idade: \033[m'))
altura = float(input('\033[1;33mDigite a sua altura (ex: 1.70): \033[m')) 
peso = float(input('\033[1;33mDigite o seu peso: \033[m'))
cidade = str(input('\033[1;33mDigite a sua cidade: \033[m'))

print('\nCalculando dados...\n')
sleep(2)

print('===== RELATÓRIO =====\n')

print(f'Nome: {nome}')
print(f'Cidade: {cidade}')
print(f'idade: {idade} anos\n')

if idade >= 18:
    situacao_idade = 'Maior de idade!'
else:
    situacao_idade = 'Menor de idade!'


print(f'Altura: {altura}')
print(f'peso: {peso}\n')
 
imc = peso / altura ** 2

if imc < 18.5:
    classificacao_imc = 'Abaixo do peso'
elif  18.5 <= imc <= 24.9:
    classificacao_imc = 'Peso normal'
elif  25 <= imc < 30:
    classificacao_imc = 'Sobre peso'
elif imc >= 30:
    classificacao_imc = 'Obesidade'
else:
    classificacao_imc = 'Não consegui calcular o IMC'

print(f'IMC: {imc:.2f}')
print(f'Classificação: {classificacao_imc}\n')

print(f'Situação de idade: {situacao_idade}\n')
