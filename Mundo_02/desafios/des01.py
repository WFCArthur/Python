print('='*30)
print('{:^30}'.format('MERCADO INTELIGENTE'))
print('='*30)

# Apresentação.
nome = str(input('Digite o seu nome: ')).capitalize()
print('~'*30)
print(f'Bem-vindo, {nome}!')

# Cadastro dos produtos, valores e quantidades.
lista_produtos = []
quant = quant_iten = acima_100 = 0
valor_total = 0

continua = 'S'


while continua == 'S':

    produto = str(input('Nome do produto: '))
    lista_produtos.append(produto)
    quant += 1

    preco = float(input('Preço:R$'))

    if preco > 100:
        acima_100 += 1

    if quant == 1:
        prec_bar = preco
        prod_bar = produto
        prec_caro = preco
        prod_caro = produto
    else:
        if prec_caro < preco:
            prec_caro = preco
            prod_caro = produto
        if prec_bar > preco:
            prec_bar = preco
            prod_bar = produto

    quantidade = int(input('Quantidade: '))
    valor_total = preco * quantidade + valor_total
    quant_iten += quantidade

    continua = str(input('Deseja adicionar mais produtos? [S/N]: ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Deseja adicionar mais produtos? [S/N]: ')).upper().strip()[0]
# Menu
while True:

    print('='*30)
    print('''[1] ver total\n[2] Ver estatísticas\n[3] pagar compra\n[4] Finalizar compra''')
    print('='*30)

    escolha = int(input('Escolha: '))
    # Estatísticas
    if escolha == 1:
        print('~'*20)
        print('{:^20}'.format('TOTAL ATUAL DA COMPRA'))
        print('~'*20)
        print('{:^20}'.format(f'Cliente: {nome}'))
        print('{:^20}'.format(f'Produtos Cadastrados: {quant}'))
        print('{:^20}'.format(f'Quantidade de itens: {quant_iten}'))
        print('{:^20}'.format(f'Valor Total: R${valor_total:.2f}'))
        print('~'*20)

    elif escolha == 2:
        print(f'Quantidade total de itens:{quant_iten}')
        print(f'Produtos cadastrados: {quant}')
        print(f'Produto mais caro: {prod_caro}')
        print(f'Produto mais barato: {prod_bar} ')
        print(f'Produtos acima de R$100: {acima_100}')
        print(f'Valor parcial: R${valor_total:.2f}')
        print('='*30)

    elif escolha == 3:

        tot_final = valor_total
        desconto = 0

        vip = str(input('Você é cliente vip? [S/N]: ')).upper().strip()[0]

        while vip not in 'SN':
            vip = str(input('Você é cliente vip? [S/N]: ')).upper().strip()[0]

        if vip == 'S':
            print('''[1] Bronze\n[2] Prata\n[3] Ouro\n''')
            nivel = int(input('Escolha: '))

            if nivel == 1:
                desconto = 0.10
            elif nivel == 2:
                desconto = 0.15
            elif nivel == 3:
                desconto = 0.20

            tot_final = valor_total - (valor_total * desconto)


        else:
            print('Qual a forma de pagamento?')
            print('''[1] Dinheiro \n[2] Pix \n[3] Cartão''')

            forma = int(input('Escolha: '))
            
            if forma == 1:
                desconto = 0.05
                tot_final = valor_total - (valor_total * desconto)

            elif forma == 2:
                desconto = 0.10
                tot_final = valor_total - (valor_total * desconto)

            elif forma == 3:
                print('''[1] Débito \n[2] Crédito \n ''')
                cartao = int(input('Escolha: '))

                if cartao == 1:
                    tot_final = valor_total

                elif cartao == 2:
                    parcela = int(input('Quantas parcelas: '))

                    if parcela <= 2:
                        tot_final = valor_total
                    else:
                        juros = 0.10
                        tot_final = valor_total + (valor_total * juros)

        print(f'Valor final calculado: R${tot_final:.2f}')

    elif escolha == 4:
        break
print('=-'*20)
print('{:^20}'.format('RELATÓRIO FINAL'))
print('=-'*20)

print(f'Cliente: {nome}')
print(f'Produtos: {lista_produtos}')

print(f'Total bruto: R$ {valor_total:.2f}')
print(f'Desconto/Juros: R$ {valor_total - tot_final:.2f}')
print(f'Valor Final: R$ {tot_final:.2f}')

print(f'Produto mais caro: {prod_caro}')
print(f'Produto mais barato: {prod_bar}')
print(f'Quantidade total: {quant_iten}')

print('='*30)
valor_pago = tot_final
ced = 200
quant_cai = 0
while True:
    if valor_pago >= ced:
        valor_pago -= ced
        quant_cai += 1
    else:
        if quant_cai > 0:
            print(f'{quant_cai} notas de R${ced}')
        quant_cai = 0
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        else:
            break