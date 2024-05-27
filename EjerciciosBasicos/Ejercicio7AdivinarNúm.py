import random

while True: 
    NumeroRand = random.randint(0,100)
    #print (NumeroRand) Se uso para verificar la correcta operación del programa
    print("Intente adivinar el numero aleatorio entre el 0 y el 100 \nEl programa le dara una pequeña ayuda haciendole saber si su numero es mayor o menor al seleccionado aleatoriamente \nSu número:")

    while True:
        Adivinar= int(input())
        
        if Adivinar>NumeroRand:
            print("Su número es mayor al aleatorio, purebe otra vez.")
            
        elif Adivinar<NumeroRand:
            print("Su número es menor al aleatorio, purebe otra vez.")
            
        else:
            print("¡Bien hecho usted ha adivinado el Número!")
            VolverAJugar = input("Desea volver a jugar? Y/N")
            break
    
     
    if VolverAJugar !='y' and VolverAJugar != 'Y':
            break
            


        
