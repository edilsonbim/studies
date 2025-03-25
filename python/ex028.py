d = int(input('Qual a distancia da sua viagem? '))
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))