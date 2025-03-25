lado1 = float(input('Digite um lado do trangulo: '))
lado2 = float(input('Digite outro lado do trangulo: '))
lado3 = float(input('Digite outro lado do trangulo: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('A figura é um triangulo é equilátero')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('A figura é um triangulo é escaleno')
    else:
        print('A figura é um triangulo é isóceles')
else:
    print('A sua figura não é um triangulo!')
