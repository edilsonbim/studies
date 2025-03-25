alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt * alt)
if imc < 18.5:
    print('Você esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você esta com peso ideal!')
elif  25 <= imc < 30:
    print('Você esta com sobrepeso!')
elif 30 <= imc < 40:
    print('Você esta com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')
