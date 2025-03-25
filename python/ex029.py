from datetime import date

ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
print('O ano {} não é BISSEXTO'.format(ano) if (4 != 0 or 100 == 0) and 400 != 0 else 'O ano {} é BISSEXTO'.format(ano))