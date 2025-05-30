vet = []
contador = 0
while contador < 5:
    num = int(input("Digite um numero para o vetor 1"))
    vet.append(num)
    contador += 1
print("Vetor 1: ", vet)

soma = 0
contador = 0
while contador < 5:
    soma = soma + vet[contador]
    contador += 1
media = soma / 5
print("Media do vetor: ", media)
