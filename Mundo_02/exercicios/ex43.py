# Desenvolvendo uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso

# Entre 18.5 e 25: Peso ideal

# 25 até 30: Sobrepeso

# 30 até 40: Obesidade

# Acima de 40: Obesidade Mórbida
from time import sleep

print('-=-'*5)
print('CALCULO DE IMC')
print('-=-'*5)

peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)
print('CARREGANDO...')
sleep(2)

print('-'*20)
if imc < 18.5:
    print(f'O IMC dessa pessoa é de {imc:.1f}')
    print('Abaixo do peso!')
elif imc < 25:
    print(f'O IMC dessa pessoa é de {imc:.1f}')
    print('Peso Ideal!')
elif imc < 30:
    print(f'O IMC dessa pessoa é de {imc:.1f}')
    print('Sobrepeso')  
elif imc < 40:
    print(f'O IMC dessa pessoa é de {imc:.1f}')
    print('Obesidade ')
else:
    print(f'O IMC dessa pessoa é de {imc:.1f}')
    print('Obesidade Mórbida, CUIDADO!')
print('-'*20)
    