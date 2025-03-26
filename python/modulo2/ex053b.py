frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
rever = junto[::-1]
#print(junto)
if rever == junto:
    print('\033[1:32:40mA frase é um palindromo!\033[m')
else:
    print('\033[1:31:40mA frase não é um palindromo!\033[m')