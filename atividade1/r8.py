numero = int(input("digite um numero >> "))
contador = 1
ultimo = 1
penultimo = 1
atual = 1

while contador <= numero: 
 
    penultimo = ultimo
    ultimo = atual 
    atual =  ultimo + penultimo
    contador = contador + 1 
    print(atual)

    