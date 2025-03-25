n = int(input('Me diga um numero qualquer: '))
resultado: int = n % 2
print('O numero {} é par.'.format(n) if resultado == 0 else 'O numero {} é ímpar.'.format(n))