# condições aninhadas!!
nome = input('Digite o seu nome: ')

if nome == 'Arthur':
    print('Que nome bonito!')
    print(f'Tenha um ótimo dia {nome}!!')
elif nome == 'Ronaldo' or nome == 'Leticia' or nome == 'Fernanda':
    print(f'{nome}, é um nome muito popular no Brasil!')
elif nome == 'Bruce':
    print('Nome de personagem de Filme! Parábens')
else:
    print('Nome totalmente normal!')
