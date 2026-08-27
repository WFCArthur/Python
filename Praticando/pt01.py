# Apresentação
print('-='*20)
print(f'{'<<< SISTEMA DE BIBLIOTECA >>>':^40}')
print('-='*20)

# Funções do programa
biblioteca = []

# Menu
while True:
    def menu_sistema():
        menu = (
        'Cadastrar livros',
        'Listar livro',
        'Buscar livro',
        'Emprestar livro',
        'Devolver livro',
        'Excluir livro',
        'Sair'
            )
        for pos,i in enumerate(menu):
            print(f'{pos+1} - {i}')

    menu_sistema()

    print('-='*20)

    escolha = int(input('Escolha: '))

    if escolha == 1:
        def cadastrar():
            livro = {}
            livro['titulo'] = str(input('Titulo: ')).capitalize()
            livro['autor'] = str(input('Autor: ')).capitalize()
            livro['ano'] = int(input('Ano: '))
            livro['disponivel'] = True

            biblioteca.append(livro)

            print('Livro cadastrado com sucesso!')
            print('-='*20)
        cadastrar()
        while True:

            opcao = str(input('Deseja continuar cadastrando? [S/N] ')).upper()[0]

            if opcao == 'N':
                break
            else:
                cadastrar()
            
    if escolha == 2:
        if len(biblioteca) == 0:
            print('~~'*20)
            print('NENHUM LIVRO CADASTRADO!')
            print('~~'*20)
        else:
            print('=='*20)
            print(f'{'Livros cadastrados':^40}')
            print('=='*20)
            for livro in biblioteca:
                for key,val in livro.items():
                    print(f'{key}: {val}')
                print('--'*20)
            print('=='*20)
    if escolha == 7:
        break
