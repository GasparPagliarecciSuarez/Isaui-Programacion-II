#Diccionario de listas: Escribe una función que tome un diccionario donde los valores
#son listas y devuelva una lista que contenga todos los elementos de las listas del
#diccionario
def Diccionario_De_Listas(diccionario):
    resultado = []
    for lista in diccionario.values():
        for elemento in lista:
            resultado.append(elemento)
    return resultado

diccionario = {
    "a": [1, 2, 3],
    "b": [4, 5],
    "c": [6, 7, 8, 9]
               }
resultado = Diccionario_De_Listas(diccionario)
print(resultado)
