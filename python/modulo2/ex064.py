n = 0
lista = []
while n != 999:
    n = int(input('Digite um numero: '))
    lista = lista + [n]
del(lista[-1])
soma = sum(lista)
print(lista)
print('A soma dos {} numeros que você digitou antes de digitar 999 foi {}.'.format(len(lista), soma))