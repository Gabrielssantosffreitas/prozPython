matriz1 = [[1,1,1],[2,2,2],[3,3,3]]
matriz2 = [[2,2,2],[3,3,3],[4,4,4]]
matriz3 =[[0,0,0],[0,0,0],[0,0,0]]
linha = 0
coluna = 0 
while linha < 3:
    while coluna < 3 :
        matriz3[linha][coluna] =  matriz1[linha][coluna] + matriz2[linha][coluna]
        coluna = coluna + 1 
    linha = linha + 1 
    coluna = 0 
print(matriz1 , "\n" , matriz2 , "\n", matriz3)
    