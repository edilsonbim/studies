maior = 0
homens = 0
m20 = 0
while True:
    print('\033[1:31m_\033[m' * 20)
    print('\033[1m Cadastre uma pessoa\033[m')
    print('\033[1:31m_\033[m' * 20)
    i = int(input('Digite a idade: '))
    while True:
        s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if s == 'M' or s == 'F':
            break
    if s == 'M':
        homens += 1
    elif s == 'F' and i > 20:
        m20 += 1
    elif i > 18:
        maior += 1
    while True:
        print('\033[1:31m_\033[m' * 20)
        x = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if x == 'S' or x == 'N':
            break
    if x == 'N':
        break
    print('\033[1m_\033[m' * 20)
print('\033[1:31m_\033[m' * 20)
print(f'\033[1:31m{maior} pessoas são maiores de 18 anos.\n{homens} pessoas são homens.\n{m20} mulheres tem menos de 20 anos.\033[m')
