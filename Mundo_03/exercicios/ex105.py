'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da Turma
- A situação (Opcional)

Adicione também as docstrings da função.'''

quant = soma = 0 
princ = []

while True:
    dado = {}
    dado['nota'] = float(input('Digite a nota: '))

    quant += 1
    soma += dado["nota"] 

    segue = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while segue not in 'SN':
        segue = str(input('Digite somente [S/N]: ')).upper()[0]
    
    princ.append(dado)
    
    if segue == 'N':
        break
    
for i,n in enumerate(princ):
    if i == 0:
        maior = menor = n["nota"]
        
    else:
        if n["nota"] > maior:
            maior = n["nota"]
        if n["nota"] < menor:
            menor = n["nota"]

media = soma / quant

print(f'Essas são as notas: {princ}')
print(f'Ao todo foram digitadas {quant} notas.')
print(f'A maior nota é {maior} e a menor {menor}.')
print(f'A média é {media:.2f}.')