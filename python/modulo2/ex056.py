m20 = 0
media = []
velho = ''
for c in range(0, 4):
    nome = str(input('Qual o nome da pessoa {}: '.format(c + 1))).upper().strip()
    idade = int(input('Qual a idade da pessoa {}: '.format(c + 1)))
    media = media + [idade]
    sexo = str(input('Qual o sexo da pessoa {}: '.format(c + 1))).upper().strip()
    if sexo[0] == 'F' and idade < 20:
        m20 = m20 + 1
    if idade >= idade and sexo == 'M':
        velho = nome
    #print(nome, idade, sexo)
#print(media)
#print(sum(media) / 4)
#print(sum(media) / 4, velho, m20)
if m20 > 1: s = 'es'
else: s = ''
print('A media de idade do grupo é {:.0f} anos, O homem mas velho é o {} e existe {} mulher{} com menos de 20 anos.'.format(sum(media) / 4, velho, m20, s))