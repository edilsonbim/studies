n = int(input('Escolha um numero: '))
for c in range(1, 11):
    print(' {} x {} = \033[1:29:48m{}\033[m '.format(n, c ,c * n))