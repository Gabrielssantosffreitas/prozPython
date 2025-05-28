primos = [1,2,3,5,7,11]
print(primos)
divisivel = 0 
numero = int(input('digite um numero > '))
contador = numero 
while  contador > 0: 
    if  numero%contador == 0 : 
        divisivel = divisivel + 1  
       

    contador = contador -1 

if divisivel <= 2 :
  
    primos.append(numero) 
print(primos)