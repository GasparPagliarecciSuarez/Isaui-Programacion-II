#Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
#devuelva la suma de todos los valores.

def Sumar_Diccionario(diccionario):
    suma=0
    for clave, valor in diccionario.items():
        if clave in diccionario:
            suma += valor

    return suma

diccionario = {
        "a":100,
        "b":1,
        "c":1,
        "d":1,
        "e":1,

}
suma = Sumar_Diccionario(diccionario)
print(suma)