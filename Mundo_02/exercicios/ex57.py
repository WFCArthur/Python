# Faça um progrma que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo [M] ou [F]: ')).upper().strip() [0]

while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite um sexo valido [M] ou [F]: ')).upper().strip()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado com sucesso.')



