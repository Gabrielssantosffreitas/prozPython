numero =  int(input("digite um numero >> "))
primo ="sim"
contador = numero
while contador >= 1:

    if numero%contador == 0: 
        print(" seu numero nao e primo")
        primo = "nao"
        break
    
if primo == "sim":
    print("seu numero e primo")   