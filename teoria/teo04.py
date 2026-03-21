frase = 'Curso em Video Python'

# print(frase[9]) # ele mostra a letra que está no indice.

# print(frase[9:14]) # mostra a frase do indice 9 ao 14.

# print(frase[:5]) # começa do indice 0  e vai até o indice 5.

# print(frase[9:21:2]) # começa do indice 9 vai até o final já que não existe o indice 21 e vai pulando de 2 em 2.

# print(frase[9::3]) #começa do indice 9 vai até o final já que não tem ponto de parada e faz isso pulando de 3 em 3.

# res = frase.upper().count('O',0,14) # conta quantas vezes aparece a letra 'O' na frase pegando do indice 0 até o 14.

# res2 = len(frase.strip()) # vai me dizer o tamanho. que é 21.

# res3 = frase.find('deo') # verifica se tem a frase 'DEO' na frase e retorna a posição que ela se encontra.

# res4 = frase.find('Android') # verifica se está na frase se não tiver retorna -1.

# es5 = 'Curso' in frase # pergunta se na frase tem a palavra curso, e retorna true ou false.

# print(res)
# print(res2)
# print(res3)
# print(res4)
# print(res5)

# res = frase.replace('Python', 'Android')
# res2 = frase.upper()
# res3 = frase.lower()
# res4 = frase.capitalize()
# res5 = frase.title()


# print(f'{res} == 1')
# print(f'{res2} == 2')
# print(f'{res3} == 3')
# print(f'{res4} == 4')
# print(f'{res5} == 5')

# frase2 = '   Aprenda Python  '

# res = frase2.strip()
# res2 = frase2.rstrip()
# res3 = frase2.lstrip()

# print(res)
# print(res2)
# print(res3)

res = frase.split()
res1 = '-'.join(frase)
res2 = len(frase.split()[3])

print(res)
print(res1)
print(res[2][3])
print(res2)

