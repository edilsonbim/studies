menu = 4
n1 = 0
n2 = 0
while menu != 5:
    if menu == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))

    menu = int(input('\nQual opção deseja? \n'
                     '1- Somar\n'
                     '2- Multiplicar\n'
                     '3- Maior\n'
                     '4- Novos numeros\n'
                     '5- Sair \n'))
    if menu == 1:
        print('A soma do numero {} + {} = {}\n'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('A multiplicação do numero {} * {} = {}\n'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O nuemro {} é maior que o {}\n'.format(n1, n2))
        elif n1 == n2:
            print('Os numeros {} e {} são iguais!\n'.format(n1, n2))
        else:
            print('O numero {} é maior que o {}\n'.format(n2, n1))
print('Fim do programa!')