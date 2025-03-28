while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f' {n} x {c} = \033[1:29:48m{c * n}\033[m ')
print('Programa encerrado. Volte sempre!')