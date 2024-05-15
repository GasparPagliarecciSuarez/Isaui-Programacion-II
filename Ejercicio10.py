import random
import re


Palabras = ["melon", "sandia", "banana", "guayaba", "manzana", "pera", "uva", "kiwi", "maracuya", "anana", "frutilla", "cereza", "durazno", 'ciruela']
PalabraRandom = random.choice(Palabras)
Vidas= 6
# desactivado, activar en caso de ser necesario para probar la funcdionalidad del programa print(PalabraRandom)
LetrasBien = ""
IntentoFinal= ""
LetrasMal = ''
cont = 0
print("Vamos a comenzar el juego del ahoracado de las frutas, ingresa una letra para comenzar a adivinar")
print("La palabra tiene: ", len(PalabraRandom),"letras")


while Vidas>=1:
        Letra = input('Ingreser su letra: ').lower()
        if re.search(Letra,PalabraRandom):
            print("Has adivinado una letra")
            LetrasBien += Letra + "_"
            print ("Tus letras se encuentran desorganizadas para aumentar la dificultad: ",LetrasBien) 
            cont += 1
            if cont==len(PalabraRandom):
                PalabraArriesgada= input("Has ingresado todas las letras corrrectas de la palabra \n Ingrese la palabra: ").lower()
                if PalabraArriesgada==PalabraRandom:
                        print("Adinivaste la palabra y Ganaste!!!", "\n \( ͡> ͜ʖ ͡<)/")
                        break
                else:
                   print("Perdiste, la palabra era:",PalabraRandom, "\n ( ͡> ︹ ͡<)")
                   break
        else:
            LetrasMal += Letra + "_"
            print("Esa letra no se encuentra dentro de la palabra: ", LetrasMal)
            
            Vidas -= 1
                 
        if Vidas==0:
            IntentoFinal= input("Desea arriesgar? (si/no): ").lower()
        
        if IntentoFinal == "si":
             PalabraArriesgada= input("Ingrese la palabra: ").lower()
             if PalabraArriesgada==PalabraRandom:
                  print("Arriesgaste y Ganaste!!!, \n \( ͡> ͜ʖ ͡<)/")
                  break
             else:
                   print("Perdiste, la palabra era:",PalabraRandom, "\n ( ͡> ︹ ͡<)")
                   break
        if IntentoFinal == "no":
             print("Perdiste, la palabra era:",PalabraRandom, "\n ( ͡> ︹ ͡<)")
             break
       