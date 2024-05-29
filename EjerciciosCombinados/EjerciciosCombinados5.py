#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva un diccionario 
#donde las claves son las letras iniciales de las palabras y los valores son listas de palabras que comienzan con esa letra.
def Palabras_Letra_Inicial(lista):
    diccionario={}

    def Separar_Letras(lista):
        letras = list(lista)
        return letras[0]
    
    for palabras in lista:
        palabras = palabras.lower()
        clave = Separar_Letras(palabras)
        
        if clave in diccionario :
             
             diccionario[clave].append(palabras)
        else:
            diccionario[clave] = [palabras]
    
    return diccionario

lista=['HOLA','como','bien', 'bueno', 'Helado', 'bailar', 'hello']

diccionario = Palabras_Letra_Inicial(lista)
print(diccionario)

