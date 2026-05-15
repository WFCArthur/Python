'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.

b) Em que posição foi digitado o primeiro valor 3.

c) Quais foram os números pares.'''

valores = ()
for v in range(0,4):
    num = (int(input('Digite um valor: ')))
    valores = valores + (num,)

print(f'Os números são {valores}')
print(f'O número nove aparece {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 03 foi digitado pela primeira vez na {valores.index(3)+1}ª posição')
else:
    print('O número 03 não foi digitado nenhuma vez.')
print('E os valores pares são ', end= '')
for n in valores:
    if n % 2 == 0:
        print(f'{n}' , end= ' ')
