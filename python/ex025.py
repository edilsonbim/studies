import random
from time import sleep

n = int(input('Escolha um numero entre 0 e 5: '))
pc = random.choice([0, 1, 2, 3, 4, 5])
pc1 = random.randint(0, 5) #outra forma de resolver
print('Processando...')
sleep(3)
if pc == n:
    print('Acertou! eu pensei exatamente no {}'.format(pc))
else:
    print('Errou! eu pensei no {}'.format(pc))
print('Acertou' if pc == n else 'Errou') #condição resumida
