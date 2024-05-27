def CONTAR_LETRAS(Lista):
    frecuencia = {}
    for letra in Lista:
            letra=letra.lower()
            if letra in frecuencia:
                frecuencia[letra] +=1
            else:
                frecuencia[letra] = 1
    
    return frecuencia


lista = input("Ingrese una oracion para poder contar la frecuencia de aparición de cada letra: ")
frecuencia = CONTAR_LETRAS(lista)
print(frecuencia)