import random
NumAdivinar = int(input("Por favor ingrese un número del 1 al 100 para que sea adivinado por el programa"))
Principio = 1
Final = 100

while Principio<=Final:
    mediana= (Principio + Final) // 2

    if mediana == NumAdivinar:
        print("El programa adivino correctamente. Tu numero era el:", NumAdivinar)
        break
    if mediana<NumAdivinar:
        print("El programa presiente que tu número es mayor al de su intento:", mediana)
        Principio = mediana + 1
    if mediana>NumAdivinar:
        print("El programa presiente que tu número es menor al de su intento:", mediana)
        Final = mediana -1 

