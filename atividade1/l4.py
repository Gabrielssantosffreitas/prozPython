vetor = [7,1,2,8,6,4,9,5,8,3,]
contador1 = 0 
contador2 = 0 
print(vetor)
while contador1 <= len(vetor):

    while contador2 < len(vetor) -1 :

       

        if vetor[contador2] > vetor[contador2 + 1]:



            valorAtualp1 = vetor[contador2]

            vetor[contador2] = vetor[contador2 + 1]

            vetor[contador2 + 1] = valorAtualp1

           
         
        contador2 = contador2 + 1

    contador2 = 0 


    contador1 = contador1 + 1

print(vetor)