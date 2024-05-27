''''Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
sin elementos duplicados.'''

def Eliminar_Duplicados(lista):
    listaNueva=[]
    
    for numero in lista:
        if numero not in listaNueva:
           listaNueva.append(numero)

    
    
    return print (listaNueva)

lista1 = [1,2,3,3,3,4,4,5,6,6,6,6,7,7,8,9]
listaNueva1=Eliminar_Duplicados(lista1)