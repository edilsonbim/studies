total = barato = mil = valor = 0
while True:
    n = str(input('Nome do produto: ')).strip().upper()
    p = float(input('Preço: R$'))
    total += p
    while True:
        c = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if valor == 0:
        barato = n
        valor = p
    if p < valor:
        valor  = p
        barato = n
    if p > 1000:
        mil += 1
    if c in 'N':
        break
    print('\033[1:32m_\033[m' * 40)
print('\033[1:31m_\033[m' * 40)
print(f'O total da compra foi de R${total:.2f}\nTemos {mil} produtos custando mais de R$1000.00\nO produto mais barato foi {barato}, que custa {valor:.2f} reais')