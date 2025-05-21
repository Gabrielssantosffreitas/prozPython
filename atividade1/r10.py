#Peça ao usuário para digitar notas até que ele digite um valor negativo. Calcule e mostre a média das
#notas digitadas
contador = 1
acumulador = 0 
soma = 0 
while contador <=2 : 
    nota = int(input(" digite um numero, para parar digite um numero negativo >> "))
    if nota < 0 : 
        break
    else: 
        soma = soma + nota 
        acumulador = acumulador + 1 

media = soma / acumulador

print(" a sua media e ",media)
# parecido com o do professor 