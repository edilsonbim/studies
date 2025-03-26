soma= 0
for c in range(0, 500, 3):
    resultado: int = c % 2
    if resultado != 0:
        soma = soma + c
        print(c)
print('\033[1:46:40mSoma: {}\033[m'.format(soma))