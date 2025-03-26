n = int(input('Escolha um numero: '))
for c in range(1, 10):
    print(' {} x {} = \033[1:29:48m{}\033[m '.format(n, c ,c * n))