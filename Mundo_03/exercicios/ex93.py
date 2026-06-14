'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dado = dict()
gols_por_partida = []
total_marcado = 0 

dado['nome'] = str(input('Nome do jogador: ')).capitalize()

partida = int(input(f'Quantas partidas o {dado["nome"]} jogou? '))

print('-='*20)

for g in range(partida):
    gol = int(input(f'   Quantos gols na {g+1}º partida? '))
    gols_por_partida.append(gol)
    dado["gols"] = gols_por_partida

    dado["total"] = sum(gols_por_partida)

print('-='*20)
print(dado)
print('-='*20)

for key,d in dado.items():
    print(f'O campo {key} tem {d}')

print('-='*20)

print(f'O jogador {dado["nome"]} jogou {partida} partidas.')

for pos,s in enumerate(gols_por_partida):
    if s == 1:
        print(f'  => Na partida {pos+1}, fez {s} gol.')
    else:
        print(f'  => Na partida {pos+1}, fez {s} gols.')
print(f'Foi um total de {dado["total"]} gols.')