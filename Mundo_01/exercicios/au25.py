# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite o sue nome:')) .strip()

res = 'silva' in nome.lower()

print(res)