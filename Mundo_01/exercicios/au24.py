# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cid = str(input('Digite um nome de uma cidade:')) .strip()

# if 'Santo' in cid.split()[0] :
    # print(True)
# else:   
    # print(False)
res = 'Santo' in cid.split()[0]

print(res)