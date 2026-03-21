# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

#A multa vai custar R$7,00 por cada km acima do limite.

velo = float(input('qual foi a velocidade do seu carro?'))

if velo > 80:
    soma = (velo - 80) * 7 # ele vai tirar 80 do total e vai multiplicar por 7.
    print(f'Você foi multado!! A velocidade permitida é de 80km/h.')
    print(f'Você terá que pagar R${soma:.2f} Reais!')
else:
    print(f'Você não foi multado! dirija sempre com cuidado!')

# Outro exemplo com a idade agora

# if idade >= 18:
   # print(f'Você tem {idade} anos, agora já pode ser preso!')
# else:
    # print(f'Você tem {idade} anos, é jovem ainda!')