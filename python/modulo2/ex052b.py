n = int(input('Digite um numero: '))
resultado = 0
for c in range(1, n + 1):
    if n % c == int():
        resultado += 1
        print('\033[1:32m{} '.format(c), end='')
    else:
        print('\033[0:31m{} '.format(c), end='')
if resultado == 2:
    print('\nEle é divisivél {} vezes e é um numero primo'.format(resultado))
else:
    print('\nEle é divisivel {} vezes e não é um numero primo'.format(resultado))
#print(resultado)
