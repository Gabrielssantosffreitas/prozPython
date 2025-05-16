numero = int(input("digite um numero >> "))
contador = 1
soma = 0 
ultimo = numero
penultimo = numero
atual = numero  

while contador <= 9: 
    print(atual)
    penultimo = ultimo
    ultimo = atual 
    atual =  ultimo + penultimo
    contador = contador + 1 

    