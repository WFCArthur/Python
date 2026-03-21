dia = int(input('Quantos dias alugados?'))

kmr = int(input('Quantos Km rodados?'))

tot = (dia * 60) + (kmr *0.15)

print(f'O total a pagar é de R${tot:.2f}')