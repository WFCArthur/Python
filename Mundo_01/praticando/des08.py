# \033[1;33m \033[m

print('====== SISTEMA DE VELOCIDADE (DETRAN) ======')

velo = int(input('Digite a velocidade do condutor: km/h '))

if velo >  80:
    limite = 80
    multa = velo - limite
    valor = multa * 7

    print(f'Condutor acima da velocidade!')
    print(f'A multa deverá ser aplicada no valor de R${valor} reais.')
    
else:
    print(f'A velocidade do condutor é {velo} km/h')
    print('Velocidade dentro do limite! DIRIJA COM CUIDADO.')

