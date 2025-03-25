n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3) / 3
print('A sua média foi {:.1f}.'.format(m))
print('Parabéns!' if m >= 6 else 'Estude mais!')