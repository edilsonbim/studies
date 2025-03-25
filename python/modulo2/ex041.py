import datetime
nasc = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - nasc
print('Com {} anos'.format(idade))
if idade <= 9:
    print('Você esta na categoria MIRIM')
elif idade <= 14:
    print('Você esta na categoria INFANTIL')
elif idade <= 19:
    print('Você esta na categoria JUNIOR')
elif idade <= 20:
    print('Você esta na categoria SENITOR')
elif idade >= 21:
    print('Você esta na categoria MASTER')
