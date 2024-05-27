def Invertir_Lista(lista):
    lista_invertida=[]
    cont_negativo=-1
    cont=1

    while cont<=len(lista):
        lista_invertida.append(lista[cont_negativo])
        cont_negativo -=1
        cont +=1

    return print("Su lista invertida es:",lista_invertida)


lista=[1,2,3,4,5,6,7,8,9]
listaInver=Invertir_Lista(lista)
