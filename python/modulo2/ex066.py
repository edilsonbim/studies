lista = []
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    lista += [n]
print(f'A media dos {len(lista)} numeros digitados é {sum(lista)/len(lista)}')