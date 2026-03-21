# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,sabendo que cada litro de tinta, pinta uma área de 2mquadra.
larg = float(input('Digite a largura que você mediu:'))
altu = float(input('Digite agora a Altura que você mediu:'))

con = larg * altu
con2 = con / 2

print(f'A largura é {larg} e a Altura é {altu}, a sua área é {con}m² e para pinta-la você precisara de {con2}L de tinta.')
