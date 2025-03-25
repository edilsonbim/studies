num = int(input('Digite um numero: '))
conv = int(input('Escolha a base de conversão \n'
                  '1 - Binário \n'
                  '2 - Octal \n'
                  '3 - Hexadecimal \n'
                 'Digite a opção desejada: '))
if conv == 1:
    print('O valor binario é o {}'.format(bin(num)))
elif conv == 2:
    print('O valor octal é o {}'.format(oct(num)))
elif conv == 3:
    print('O valor hexadecimal é o {}'.format(hex(num)))

