#Solicite dois números ao usuário e mostre todos os números pares entre esses dois valores
numero1 = int(input("digite um numero >> "))
numero2 = int(input("digite um numero >> "))


contador = numero1
while contador <= numero2: 
    if contador%2 == 0 :
        print(contador )
    else:
        print("")

    contador = contador +1

