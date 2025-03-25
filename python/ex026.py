km = int(input('Qual a velocidade do carro? '))
if km > 80:
    print('Voce foi multado! exedeu o limite permitido de 80km/h \n'
          'Você deve pagar uma multa de R${:.2f}.'.format((km - 80) * 7))
else:
    print('Tenha um bom dia e dirija com segurança!')