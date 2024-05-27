import random

LongClave=int(input("Ingrese la longitud deseada para su clave aleatoria. \n(La misma no puede ser menor a 12 caracteres y tampoco puede ser mayor a 20) \n: "))
if LongClave < 12 or LongClave > 20:
    print("La longitud de la clave debe estar entre 12 y 20 caracteres.")
else:
    clave = ''
    

    #for _ in range(LongClave) :
    while len(clave) < LongClave :
        clave += random.choice('0123456789')
        clave += random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
        clave += random.choice('qwertyuiopasdfghjklzxcvbnm')
        clave += random.choice('!@#$%^&*')
       
        if len(clave) == LongClave:
            break
    print("Su clave aleatoria es:", clave, "\nPSSS no la comparta con nadie ;)")