'''Contar palabras en frases: Escribe una función que reciba una lista de frases y
devuelva un diccionario donde las claves son las palabras y los valores son las
frecuencias de esas palabras en todas las frases.'''
def Contar_Palabras_En_Frases(lista):
    diccionario = {}
    for frase in lista:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1
    return diccionario

frases = ["Hola todo bien ?", "Hola bien y vos ?", "bien tambien"]
resultado = Contar_Palabras_En_Frases(frases)
print(resultado)