#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.

def frecuencia(lista):
    diccFrec={}
    for i in lista:
        if i in diccFrec:
            diccFrec[i] +=1
        else :
            diccFrec[i] = 1
    return print (diccFrec)


lista= ["hola", "buenas", "chau", "tardes", "hola", "hola"]
frec= frecuencia(lista)
