# Desenvolva um programa que pergunte a distância de uma viagem em Km.

# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

viagem = float(input('Qual é a distancia da viagem a ser feita? KM'))

print(f'Você fará uma viagem de {viagem:.1f}Km.')

if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print(f'Você pagará um valor de R${preço:.2f} Reais.')
    
