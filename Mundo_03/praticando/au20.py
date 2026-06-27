'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B é = {s}')

# programa principal.
soma(5,1)'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2,3,4,5,7)
contador(8,2,3)
contador(6,1,2,3,9)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1

valores = [2,6,5,9,10]
dobra(valores)
print(valores)'''

def soma(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}')

soma(3,4,5)
soma(2,8,1,9)
