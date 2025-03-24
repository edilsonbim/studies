nome = input('Digite seu nome completo: ')
print('Analizando seu nome... \n'
      ' Seu nome em maiusculas é {} \n'
      ' Seu nome em minusculas é {} \n'
      ' Seu nome tem ao todo {} letras \n'
      ' Seu primeiro nome é {} e ele tem {} letras'.format(nome.upper(),nome.lower(),len(nome) - nome.count(' '),nome.strip().split()[0],len(nome.strip().split()[0])))
