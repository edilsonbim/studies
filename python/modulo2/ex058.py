import random
from time import sleep
pc = random.randint(0, 10)
n = 11
while pc != n:
    n = int(input('Escolha um numero entre 0 e 10: '))
    print('Processando...')
    sleep(1)
    if pc != n: print('Errou! eu pensei em outro numero, tente novamente!')
print('Acertou! eu pensei exatamente no {}'.format(pc))
