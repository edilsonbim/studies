import datetime
nasc = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - nasc
print('Com {} anos'.format(idade))
if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade <= 25:
    print('Você está na categoria SENIOR')
elif idade > 25:
    print('Você está na categoria MASTER')
