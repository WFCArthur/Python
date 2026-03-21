# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
valor01 = float(input('Eu consigo converter metros em centímetros e também em milímetros.\nQuantos metros você quer que eu converta? '))

centimetros = valor01 * 100
milimetros = valor01 * 1000

print(f'O valor digitado foi {valor01} metro(s).')
print(f'Convertendo em centímetros fica {centimetros} cm.')
print(f'Convertendo em milímetros fica {milimetros} mm.')