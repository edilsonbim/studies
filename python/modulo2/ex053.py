frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
count = len(frase) -1
rever = ''
for c in range(0, len(frase)):
    #print(frase[c])
    #print(frase[count])
    rever = rever + frase[count]
    count = count - 1
#print(rever)
if rever == frase:
    print('\033[1:32:40mA frase é um palindromo!\033[m')
else:
    print('\033[1:31:40mA frase não é um palindromo!\033[m')
