num1 = int(input('DIgite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero {} é maior que o numero {}'.format(num1, num2))
elif num1 < num2:
    print('O numero {} é menor que o numero {}'.format(num1, num2))
elif num1 == num2:
    print('O numero {} e o numero {} são iguais'.format(num1, num2))