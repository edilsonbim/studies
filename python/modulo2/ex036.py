casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
anos = int(input('Digite em quantos anos voce quer pagar: ')) * 12
parcela = casa / anos
if parcela <= salario * 0.3:
    print('Financiamento aprovado! o valor da sua parcela é de R${:.2f}.'.format(parcela))
else:
    print('Financiamento negado! infelizmente o valor da parcela de R${:.2f}, ultrapassa 30% do seu salário.'.format(parcela))
