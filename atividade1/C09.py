# entrada 
preco = int(input("digite o valor >> "))
# processamento 
if preco >= 100:
    print("o preco com  descoto e de ", ((10/100*preco) - preco)*-1 )
#saida 
else:
    print("vc nao tem descoto")