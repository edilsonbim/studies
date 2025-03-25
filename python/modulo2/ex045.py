import random
from time import sleep
escolha = int(input('1 - Pedra'
                    '\n2 - Papel '
                    '\n3 - Tesoura'
                    '\nEscolha a opção: '))
pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
vc = 'Pedra' if escolha == 1 else 'Papel' if escolha == 2 else 'Tesoura'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('\033[1:30:46m-=\033[m' * 12)
print('O computador jogou {}\nVocê jogou {}.'.format(pc, vc))
if pc == vc:
    print('\033[1:30:44mEmpate!\033[m')
if pc == 'Pedra' and vc == 'Tesoura':
    print('\033[1:30:41mPerdeu!\033[m')
elif pc == 'Pedra' and vc == 'Papel':
    print('\033[1:30:42mGanhou!\033[m')
elif pc == 'Papel' and vc == 'Tesoura':
    print('\033[1:30:42mGanhou!\033[m')
elif pc == 'Papel' and vc == 'Pedra':
    print('\033[1:30:41mPerdeu!\033[m')
elif pc == 'Tesoura' and vc == 'Pedra':
    print('\033[1:30:42mGanhou!\033[m')
elif pc == 'Tesoura' and vc == 'Papel':
    print('\033[1:30:41mPerdeu!\033[m')
print('\033[1:30:46m-=\033[m' * 12)
