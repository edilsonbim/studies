nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('Parabéns você foi aprovado!')
elif 5 <= media < 7:
    print('Atenção, você ficou de recuperação!')
elif media < 5:
    print('Infelizmente você foi reprovado!')
print('Sua média foi de {:.2f}'.format(media))
