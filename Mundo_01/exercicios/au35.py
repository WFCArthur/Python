# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas pdem ou não formar um triângulo.

# a + b > c, \quad a + c > b, \quad b + c > a

r1 = float(input('Digite o primeiro comprimento da reta:'))
r2 = float(input('Digite o segundo comprimento da reta:'))
r3 = float(input('Digite o terceiro comprimento da reta:'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triangulo!!')
else:
    print('As retas não podem formar um triangulo!!')
    