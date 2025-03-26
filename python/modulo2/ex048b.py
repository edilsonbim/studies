soma= 0
for c in range(0, 500):
    resultado: int = c % 2
    resultadob: int = c % 3
    if resultado != 0 and resultadob == 0:
        soma = soma + c
        print(c)
print('\033[1:46:40mSoma: {}\033[m'.format(soma))