n = int(input('Escolha um numero: '))
x = int(input('Escolha a quantidade de elementos: '))
lista = [0] + [n]
print('{} {} '.format(lista[0],lista[1]), end='')
while x != 0:
    x -= 1
    lista += [lista[-1] + lista[-2]]
    print('{} '.format(lista[-1]), end='')
print(lista)
