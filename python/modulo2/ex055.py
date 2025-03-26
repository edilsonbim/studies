a = []
for c in range(0, 5):
    a = [float(input('Qual o peso da pessoa {}: '.format(c + 1)))] + a
a.sort()
print('\033[1:29:40mA pessoa mais leve pesa {}Kg, e a mais pesada pesa {}Kg.\033[m'.format(a[0], a[len(a)-1]))
