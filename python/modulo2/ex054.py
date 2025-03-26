import datetime
pessoas = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    if datetime.date.today().year - nasc >= 21:
        pessoas += 1
    print('Pessoa {} tem {} anos'.format(c+1, datetime.date.today().year - nasc))
if pessoas == 6:
    print('{} pessoa ainda não é maior de 21 anos de idade.'.format(7 - pessoas))
elif pessoas == 7:
    print('Todas as pessoas são maiores de 21 anos de idade.'.format(7 - pessoas))
else:
    print('{} pessoas ainda não são maiores de 21 anos de idade.'.format(7 - pessoas))
