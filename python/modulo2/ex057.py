sexo = ''
while sexo != 'M' and sexo != 'F':
     sexo = str(input('Qual seu sexo? Digite [M/F]: ')).upper().strip()[0]
     if sexo != 'M'and sexo != 'F':
        print('Sexo nao reconhecido. Tente novamente.')
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print('Sexo \033[1m{}\033[m cadastrado com sucesso.'.format(sexo))
