vetor = [1,2,3,4,5,6,7,7,7,7,7,4,3,2,1,1,1,9,9,1,2,3,3,3,4,4,4,5,5,5,6,6,7,8,8,99,0]
print(vetor)
num = int(input("digite um numero de 0 a 9 para verificar quantas vezes ele aparece no vetor "))
quantidade = 0
contador = 0
while contador < len(vetor):
    if vetor[contador] == num: 
        quantidade = quantidade + 1
    contador = contador + 1
print(" esse numero aparece ", quantidade)