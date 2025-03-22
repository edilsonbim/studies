preco = float(input("Qual o valor do produto? R$ "))
desconto = float(input('Qual a porcentagem do desconto? '))
novo = preco -preco * desconto/100
print('O valor do produto com desconto é de R${:.2f} '.format(novo))