import random
from time import sleep
pc = random.randint(0, 10)
n = 11
count = 0
while pc != n:
    n = int(input('Escolha um numero entre 0 e 10: '))
    print('Processando...')
    sleep(1)
    if pc != n:
        count += 1
        print('Errou! eu pensei em outro numero, tente novamente!')
print('Acertou! eu pensei exatamente no {}. Você precisou de {} tentativas.'.format(pc, count))
