num=int(input("Ingrese el número del cual desea conocer su factorial: "))
contador = 1
suma = 0
factorial = 1
while contador<=num:
    factorial*= contador
    contador+= 1

print("El factorial de", num, "es:", factorial)
