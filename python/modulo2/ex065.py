x = 'S'
lista = []
while x == 'S':
    n = float(input('Digite um numero: '))
    lista = lista + [n]
    x = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print(lista)
print('A media dos {} numeros digitados é {:.2f}'.format(len(lista), sum(lista) / len(lista)))
