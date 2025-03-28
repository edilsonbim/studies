print('\033[1:31m=\033[m' * 12)
print('BANCO BIM')
print('\033[1:31m=\033[m' * 12)
saldo = int(input('Qual valor você quer sacar?: R$'))
cinquenta = saldo // 50
saldo -= cinquenta * 50
vinte = saldo // 20
saldo -= vinte * 20
dez = saldo // 10
saldo -= dez * 10
um = saldo // 1
saldo -= um * 1
print('\033[1:31m=\033[m' * 12)
print(f'Total de {cinquenta} notas de R$50')
print(f'Total de {vinte} notas de R$20')
print(f'Total de {dez} notas de R$10')
print(f'Total de {um} notas de R$1')
#print(saldo)
