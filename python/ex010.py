# 60 por dia e 0,15 por km
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (dias * 60) + (km * 0.15)
print("O valor do aluguel a pagar é de R$ {}".format(valor))