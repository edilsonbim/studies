n = int(input('Escolha um numero: '))
r = int(input('Escolha ua razão aritimética: '))
l = []
for c in range(0, 10):
    l = l + [n + r * c]
print(l)