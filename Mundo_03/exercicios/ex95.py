'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

princ = list()
dados = dict()

while True:
    dados['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou: '))

    gols_por_partida = []

    for p in range(partidas):
        gol = int(input(f'  Quantos gols na {p+1}º partida: '))
        gols_por_partida.append(gol)

    dados['gols'] = gols_por_partida.copy()
    dados['total'] = sum(gols_por_partida)
    princ.append(dados.copy())

    res = str(input('Deseja cadastrar mais: [S/N] ')).upper()[0]
    while res not in 'SN':
        res = str(input('Tente novamente: [S/N] ')).upper()[0]
    print('-='*20)
    if res == 'N':
        break

print(f'{"cod":<5}{"nome":<10}{"gols":<15}{"total":<10}')
print(f'-='*20)
for pos,j in enumerate(princ):
    print(f'{pos:<5}{j["nome"]:<10}{str(j["gols"]):<15}{j["total"]:<10}')
print(f'-='*20)

while True:
    apro = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if apro == 999:
        break

    if apro < 0 or apro >= len(princ):
        print(f'ERRO! Não existe jogador com código {apro}')
    else:
        print(f'-- Levantamento do jogador {princ[apro]["nome"]}')
        for pos,i in enumerate(princ[apro]["gols"]):
            print(f'   No jogo {pos + 1} fez {i} gols.')
    print('-='*20)
print('<<< Volte Sempre >>>')
