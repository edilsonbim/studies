print('\033[1:31m=\033[m' * 12)
print('BANCO BIM')
print('\033[1:31m=\033[m' * 12)
saldo = int(input('Qual valor você quer sacar?: R$'))
c = saldo // 50
saldo -= c * 50
v = saldo // 20
saldo -= v * 20
d = saldo // 10
saldo -= d * 10
u = saldo // 1
saldo -= u * 1
print('\033[1:31m=\033[m' * 12)
print(f'Total de {c} notas de R$50')
print(f'Total de {v} notas de R$20')
print(f'Total de {d} notas de R$10')
print(f'Total de {u} notas de R$1')
#print(saldo)
