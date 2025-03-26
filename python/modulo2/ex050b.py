l = 0
for c in range(0, 6):
    n = int(input('{}-Escolha um numero: '.format(c + 1)))
    resultado: int = n % 2
    if resultado == 0:
        l= l + n
print('A soma dos numeros pares é {}.'.format(l))