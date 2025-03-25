n = int(input('Me diga um numero qualquer: '))
resultado = n % 2
print('O numero {} é par.'.format(n) if resultado == 0 else 'O numero {} é impar.'.format(n))