n = int(input('Escolha um numero: '))
x = int(input('Escolha a quantidade de elementos: '))
lista = [0] + [n]
while x != 0:
    x -= 1
    lista = lista + [lista[-1] + lista[-2]]
print(lista)
