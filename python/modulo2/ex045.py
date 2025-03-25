import random

escolha = int(input('1 - Pedra'
                    '\n2 - Papel '
                    '\n3 - Tesoura'
                    '\nEscolha a opção: '))
pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
vc = 'Pedra' if escolha == 1 else 'Papel' if escolha == 2 else 'Tesoura'
print('O computador jogou {}\nVocê jogou {}.'.format(pc, vc))
if pc == vc:
    print('Empate!')
if pc == 'Pedra' and vc == 'Tesoura':
    print('Perdeu!')
elif pc == 'Pedra' and vc == 'Papel':
    print('Ganhou!')
elif pc == 'Papel' and vc == 'Tesoura':
    print('Ganhou!')
elif pc == 'Papel' and vc == 'Pedra':
    print('Perdeu!')
elif pc == 'Tesoura' and vc == 'Pedra':
    print('Ganhou!')
elif pc == 'Tesoura' and vc == 'Papel':
    print('Perdeu!')
