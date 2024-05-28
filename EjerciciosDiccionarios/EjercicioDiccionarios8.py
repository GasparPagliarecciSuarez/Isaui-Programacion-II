#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.
def Diccionario_Frecuencias(lista):
    diccFrec={}
    for palabras in lista:
        if palabras in diccFrec:
            diccFrec[palabras] +=1
        else:
            diccFrec[palabras] = 1
           
    print (diccFrec)
    return print (diccFrec)


lista= ["hola", "buenas", "chau", "tardes", "hola", "hola", '']
frec= Diccionario_Frecuencias(lista)


        
   



