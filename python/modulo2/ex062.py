n = int(input('Escolha um numero: '))
r = int(input('Escolha ua razão aritimética: '))
l = []
while len(l) < 10:
    l = l + [n + r * len(l)]
print(l)
m = int(input('Digite quantos termos extra quer gerar: '))
while len(l) < 10 + m:
    l = l + [n + r * len(l)]
print(l)
