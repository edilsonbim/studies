salario = int(input('Qual o salario do funcionario? '))
if salario < 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10
print('Quem ganahava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))