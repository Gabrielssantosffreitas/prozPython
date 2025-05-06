valor = float(input("qual é o valor"))
porcentagem = int(input("qual é a porcentagem do desconto"))
desconto = (porcentagem/100) * valor
valor_com_desconto_aplicado = valor-desconto
print(valor_com_desconto_aplicado)