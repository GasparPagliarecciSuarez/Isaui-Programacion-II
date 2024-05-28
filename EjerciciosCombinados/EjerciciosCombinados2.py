#Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
#un diccionario donde las claves son las longitudes de las palabras y los valores son
#listas de palabras con esa longitud.

def Agrupar_Por_Longitud(lista):
    diccionario = {}
    for palabra in lista:
        longitud = len(palabra)
        if longitud in diccionario:
            diccionario[longitud].append(palabra)
        else:
            diccionario[longitud] = [palabra]
    return diccionario

palabras = ["hola", "bien", "vos", "como", "estas", "chau"]
resultado = Agrupar_Por_Longitud(palabras)
print(resultado)