numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um numero entre 0 e 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {numero[escolha]}')