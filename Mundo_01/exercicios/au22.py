# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas.

# O nome com todas minúculas.

# Quantas letras ao todo(sem considerar espaços).

# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome:'))

mai = nome.upper()
min = nome.lower()
tot = len(nome.strip())
totp = len(nome.split()[0])

print(f'O seu nome com todas as letras MAIUSCULAS {mai}!')
print(f'O seu nome com todas as letras minusculas {min}!')
print(f'Quantas letras no total {tot}!')
print(f'e quantas letras tem o primeiro nome {totp}!')
