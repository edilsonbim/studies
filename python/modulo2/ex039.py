import datetime
nasc = int(input('Digite o ano do seu nascimento: '))
hj = datetime.date.today().year
alist = hj - nasc
if alist < 18:
    print('Voce deve se alistar no ano de {}, daqui {} anos.'.format(18 - alist + hj, 18 - alist))
elif alist == 18:
    print('Voce deve se alistar este ano de {}'.format(hj))
elif alist > 18:
    print('Voce deveria ter se alistado em {}, esta atrasado em {} anos.'.format(nasc + 18, nasc + 18 - hj), )
