# entrada 
lado1 = int(input("digite o valor do lado >> "))
lado2 = int(input("digite o valor do lado >> "))
lado3 = int(input("digite o valor do lado >> "))
# processamento 
if lado1 == lado2 and lado2 == lado3: 
    #saida 
    print("triangulo equilatero ")
if lado1 != lado2 and lado2 != lado3 and lado3 != lado1 : 
    print("esse triagulo e escaleno")
else: 
    print("esse triagulo e isoceles ")