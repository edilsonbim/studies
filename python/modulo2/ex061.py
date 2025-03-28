n = int(input('Escolha um numero: '))
r = int(input('Escolha ua razão aritimética: '))
l = []
while len(l) < 10:
    l  += [n + r * len(l)]
print(l)