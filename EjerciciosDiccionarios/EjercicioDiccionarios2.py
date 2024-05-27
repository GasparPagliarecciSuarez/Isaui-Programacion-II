def Invertir(diccionario):
    diccionario_invertido = {}
    print("Ingrese los pares clave-valor. Escriba 'fin' para terminar.")
    while True:
        clave = input("Ingrese la clave:")
        if clave.lower() == 'fin':
            break
        valor = input("Ingrese el valor:")
        if valor.lower() == 'fin':
            break
        diccionario_invertido[valor] = clave

    return diccionario_invertido

diccionario = {}
diccionario = Invertir(diccionario)
print("Diccionario invertido:", diccionario)