vet1 = []
vet2 = []
vet3 = []

contador = 0
while contador < 5:
    num = int(input("Digite um numero para o vetor 1"))
    vet1.append(num)
    contador += 1
print("Vetor 1: ", vet1)

contador = 0
while contador < 5:
    num = int(input("Digite um numero para o vetor 2"))
    vet2.append(num)
    contador += 1
print("Vetor 2: ", vet2)

contador = 0
while contador < 5:
    soma = vet1[contador] + vet2[contador]
    vet3.append(soma)
    contador += 1
print("Vetor 3: ", vet3)
