# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# Último = Souza

nome = str(input('Digite o seu nome:')). strip()

pris = nome.split()

print(f'primeiro: {pris[0]}')
print(f'segundo: {pris[-1]}')