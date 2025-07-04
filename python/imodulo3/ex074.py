from random import randint
tabela = []
for n in range(5):
    tabela = tabela + [randint(1,9)]
print(tabela)
print(f'O maior valor sorteado foi {max(tabela)}')
print(f'O menor valor sorteado foi {min(tabela)}')