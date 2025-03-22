saque = 0
saldo = 110
valor = 0
deposito = 0
menu = input('Digite a opção que deseja: saldo, saque, deposito?')
if menu == 'saldo': print('Saldo atual R$',saldo)
if menu == 'saque': valor = int(input('Digite o valor da saque: '))
if valor > saldo: print ('Saldo insuficiente')
if valor <= saldo: saldo = int(saldo-valor)
print('Saldo atual R$',saldo)
if menu == "deposito": deposito = int(input('Digite o valor da deposito: '))
if deposito > 0: saldo = int(saldo+deposito)
print('Saldo atual R$',saldo)
