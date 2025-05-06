nota1 = int(input("digite sua primeira nota"))
peso_da_nota1 = int(input("digite o peso da sua primeira nota"))

nota2 = int(input("digite sua segunda nota"))
peso_da_nota2 = int(input("digite o peso da sua segunda nota"))

nota3 = int(input("digite sua terceira nota"))
peso_da_nota3 = int(input("digite o peso da sua terceira nota"))

soma_das_notas = (nota1*peso_da_nota1) + (nota2*peso_da_nota2) + (nota3*peso_da_nota3)
media = soma_das_notas/ (peso_da_nota1+peso_da_nota2+peso_da_nota3)

print(media)
