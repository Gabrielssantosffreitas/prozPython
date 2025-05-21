
numero = int(input("digite um numero >> "))

contador = numero - 1 

primo = "sim"

while contador >=2: 
    print(contador)

    if numero%contador == 0:
        print("Esse numero não e primo")
        primo = "nao"
        contador = 2 

    contador = contador - 1
if primo == "sim":
    print("Esse e primo")

# res