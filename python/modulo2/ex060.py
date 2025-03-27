n = int(input('\nDigite um numero: '))
x = n
y = n
lista = []
while x > 0:
    n = n * (x-1)
    x -= 1
    lista = lista + [n]
del(lista[-1])
print(lista)
print('O fatorial de {} é {}.'.format(y, lista[-1]))
