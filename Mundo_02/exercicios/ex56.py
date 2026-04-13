# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma_idades = 0
mais_velho = 0          # variáveis para armazenar informações do programa
nome_mais_velho = ''
mulher = 0
idade = 0

for n in range(1,5):

    print(f'----- {n}ª pessoa -----')

    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: ')) # fazendo as perguntas.
    sexo = input('Digite o seu sexo: [F] ou [M] ').upper()
    soma_idades += idade

    if sexo == 'M' and idade > mais_velho:
        nome_mais_velho = nome    # verificando a idade do homem mais velho e descobrindo qual o seu nome.
        idade_v = idade
        
    if sexo == 'F' and idade < 20: # verificando quantas mulheres tem menos 20 anos.
        mulher += 1             
                            
media = soma_idades / 4 # Calculando a média de idades.
    
print(f'a média de idade {media:.1f}.')
print(f'O nome do homem mais velho é {nome_mais_velho} com {idade_v} anos.') # resultado.
print(f'E tem {mulher} mulheres com menos de 20 anos.')