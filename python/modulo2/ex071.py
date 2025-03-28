print('\033[1:31m=\033[m' * 30)
print(f'{'BANCO BIM':^30}')
print('\033[1:31m=\033[m' * 30)
saldo = int(input('Qual valor você quer sacar?: R$'))
cinquenta = saldo // 50
saldo -= cinquenta * 50
vinte = saldo // 20
saldo -= vinte * 20
dez = saldo // 10
saldo -= dez * 10
um = saldo // 1
saldo -= um * 1
print('\033[1:31m=\033[m' * 30)
if cinquenta > 0:
    print(f'Total de {cinquenta} notas de R$50')
if vinte > 0:
    print(f'Total de {vinte} notas de R$20')
if dez > 0:
    print(f'Total de {dez} notas de R$10')
if um > 0:
    print(f'Total de {um} notas de R$1')
print('\033[1:31m=\033[m' * 30)
print(f'{'Volte sempre ao BANCO BIM! um bom dia!':^30}')
print('\033[1:31m=\033[m' * 30)
#print(saldo)
