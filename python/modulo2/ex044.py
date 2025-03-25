valor = float(input('Digite o valor do produto: '))
opcao = int(input('Qual a forma de pagamento? \n'
      '1 - A vista\n'
      '2 - A vista no cartão\n'
      '3 - em até 2x no cartão\n'
      '4 - 3x ou mais\n'
      'Digite a opção: '))
parcela = valor
if opcao == 1:
    parcela = valor * 0.9
elif opcao == 2:
    parcela = valor * 0.95
elif opcao == 3:
    parcela = valor * 1
    print('O valor de cada parcela vai ser de R${:.2f}'.format(parcela / 2))
elif opcao == 4:
    x = int(input('Digite a quantidade de parcelas: '))
    parcela = valor * 1.2
    print('O valor de cada parcela vai ser de R${:.2f}'.format(parcela / x))
print('O valor total do produto vai ser R${:.2f}'.format(parcela))
