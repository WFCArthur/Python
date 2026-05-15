'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética. => sorted
d) Em que posição na tabela está o time da Chapecoense.'''

# Tabela do Brasileirão 2026
tab = ('Palmeiras','Flamengo','Fluminense','São Paulo',
'Athletico-PR','Bahia','Bragantino','Vasco da Gama',
'Curitiba','EC Vitória','Cruzeiro','Botafogo',
'Atlético MG','Internacional','Santos','Corinthians',
'Grêmio','Mirassol','Remo','Chapecoense')


print('\033[1;32m=-\033[m'*20)
print(f'\033[1;37mLista do Brasileirão\033[m \033[0;37m{tab}\033[m.')
# Os 5 primeiros da tabela.
print('\033[1;32m=-\033[m'*20)
print(f'\033[1;37mOs 5 primeiros\033[m \033[0;37m{tab[0:5]}\033[m.')
# Os 4 ultimos da tabela.
print('\033[1;32m=-\033[m'*20)
print(f'\033[1;37mOs 4 ultimos\033[m \033[0;37m{tab[-4:]}\033[m.')
# A tabela em ordem alfabética.
print('\033[1;32m=-\033[m'*20)
print(f'\033[1;37mEm ordem\033[m \033[0;37m{sorted(tab)}\033[m.')
# Em que posição está a Chapecoense.
print('\033[1;32m=-\033[m'*20)
print(f'\033[1;37mE o time da Chapecoense está em {tab.index("Chapecoense")+1}ª lugar da tabela.\033[m')