from random import randint
while True:
    vc = int(input('Digite um valor: '))
    pc = randint(1, 11)
    pi = str(input('Digite par ou ímpar: ')).upper().strip()[0]
    soma = (vc + pc) % 2
    if pi == 'P' and soma == 0:
        print(f'Você ganhou! {vc} + {pc} = {vc + pc}')
    if pi == 'I' and soma == 1:
        print(f'Você ganhou! {vc} + {pc} = {vc + pc}')
    elif pi == 'P' and soma == 1 or pi == 'I' and soma == 0:
        print(f'Você perdeu! {vc} + {pc} = {vc + pc}')
        break


