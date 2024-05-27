#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.
def Diccionario_Frecuencias(lista):
    diccFrec={}
    clave = ""
    cont = 0
    valor = 0
    contpal= 0
    for palabras in lista:
        clave = palabras
        for palabras in lista:
            if palabras in lista:
                diccFrec[clave] = cont
                cont +=1
               
            
        
        

    resultado = cont
    print (diccFrec)
    return print (resultado)


lista= ["hola", "buenas", "chau", "tardes", "hola", "hola"]
frec= Diccionario_Frecuencias(lista)

        
   



