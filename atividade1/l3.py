vetor1 = [1,2,10,4,5]
maiorNumero = 0 
contador = 0 
while contador < 5: 
    ponteiro = vetor1[contador]
    if ponteiro > maiorNumero: 
        maiorNumero = ponteiro
    contador = contador + 1
print(vetor1)
print(maiorNumero)
