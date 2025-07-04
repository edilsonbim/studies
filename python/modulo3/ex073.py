tabela = 'Internacional', 'Corinthians', 'Ceará', 'Fortaleza', 'Botafogo', 'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio', 'Vasco', 'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport Recife', 'Atletico-MG', 'Vitoria'
print('\nTabela Brasileirão')
for pos, c in enumerate(tabela):
    print(f'{pos+1} - {c}')
print('\nOs 5 primeiros são:')
for c in range(0, 5):
    print(f'{c+1} - {tabela[c]}')
print('\nOs 4 ultimos são:')
for c in range(17, 21 ):
    print(f'{c} - {tabela[c-1]}')
print('\nTimes em ordem alfabetica:')
for a in sorted(tabela):
    print(f' - {a}')

print(f'\nO Cruzeiro está na {tabela.index('Cruzeiro')}ª posição')

