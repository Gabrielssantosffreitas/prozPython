numero = 10 
contador = 0
while contador <= 1 : 
    chute = int(input("digite um numero >> "))
    if chute == 10:
        print("vc acertou !!!!!!")
        contador = contador + 1
    elif chute < 10: 
        print("muito baixo tente dnv")
    elif chute > 10 : 
        print("muito alto chute dnv")