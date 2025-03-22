salario = float(input('Qual o valor atual do salario do funcionario? '))
novo = float(input('Qual a porcentagem do aumento? '))
print("O funcionario que ganahava {}, com o aumento de {}%, agora vai passar a receber R$ {}." .format(salario, novo, (salario +salario * novo/100)))

