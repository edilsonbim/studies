salario = int(input('Qual o salario do funcionario? '))
if salario < 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10
# \033[0:30:41m para mudar a cor, e \033[m pra voltar original
# style none = 0
# boold = 1
# underline = 4
# negative = 7
print('Quem ganahava \033[0:30:41mR${:.2f}\033[m passa a ganhar \033[0:29:42mR${:.2f}\033[m agora.'.format(salario, aumento))