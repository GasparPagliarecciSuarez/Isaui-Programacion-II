def AGREGAR_ESPACIO(texto):
    LongTxt= len(texto)
    cont = 0
    textoConEspacio=""
    while cont < LongTxt:
        textoConEspacio += texto[cont] + " " 
        cont += 1
       
    return textoConEspacio


texto=input("Ingrese un texto:")
textoConEspacios = AGREGAR_ESPACIO(texto)
print("Su texto espaciado es:", textoConEspacios)




