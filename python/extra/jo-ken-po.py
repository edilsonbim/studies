import random
from time import sleep
placarvc = 0
placarpc = 0
e = 5
for c in range(0, 5):
    escolha = int(input('1 - Pedra'
                        '\n2 - Papel '
                        '\n3 - Tesoura'
                        '\nEscolha a opção: '))
    pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
    vc = 'Pedra' if escolha == 1 else 'Tesoura' if escolha != 2 else 'Papel'
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    print('\033[1:30:46m-=\033[m' * 12)
    print('O computador jogou {}\nVocê jogou {}.'.format(pc, vc))
    if pc == vc:
        print('\033[1:30:44mEmpate!\033[m')
        c = c - 1
    if pc == 'Pedra' and vc == 'Tesoura':
        print('\033[1:30:41mPerdeu!\033[m')
        placarpc = placarpc + 1
    elif pc == 'Pedra' and vc == 'Papel':
        print('\033[1:30:42mGanhou!\033[m')
        placarvc = placarvc + 1
    elif pc == 'Papel' and vc == 'Tesoura':
        print('\033[1:30:42mGanhou!\033[m')
        placarvc = placarvc + 1
    elif pc == 'Papel' and vc == 'Pedra':
        print('\033[1:30:41mPerdeu!\033[m')
        placarpc = placarpc + 1
    elif pc == 'Tesoura' and vc == 'Pedra':
        print('\033[1:30:42mGanhou!\033[m')
        placarvc = placarvc + 1
    elif pc == 'Tesoura' and vc == 'Papel':
        print('\033[1:30:41mPerdeu!\033[m')
        placarpc = placarpc + 1
    print('\033[1:30:46m-=\033[m' * 12)
    print('     \033[2:30:45m{} CPU x VOCE {}\033[m     '.format(placarpc,placarvc))
    print(c)
