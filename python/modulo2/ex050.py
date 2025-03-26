l = 0
n1 = int(input('1-Escolha um numero: '))
resultado: int = n1 % 2
if resultado == 0:
    l= l +n1
n2 = int(input('2-Escolha um numero: '))
resultado: int = n2 % 2
if resultado == 0:
    l= l +n1
n3 = int(input('3-Escolha um numero: '))
resultado: int = n3 % 2
if resultado == 0:
    l= l +n1
n4 = int(input('4-Escolha um numero: '))
resultado: int = n4 % 2
if resultado == 0:
    l= l +n1
n5 = int(input('5-Escolha um numero: '))
resultado: int = n5 % 2
if resultado == 0:
    l= l +n1
n6 = int(input('6-Escolha um numero: '))
resultado: int = n6 % 2
if resultado == 0:
    l= l +n1
print('A soma dos numeros pares é {}.'.format(l))