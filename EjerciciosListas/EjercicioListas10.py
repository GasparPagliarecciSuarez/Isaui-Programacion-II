#Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.
def Encontrar_Indice(lista,n):
    cont = 0
    for elemento in lista:
        if elemento == n:
           return cont
    
        cont +=1
    else:
            return-1

    
lista= [1,3,2,3,4,4,5,6,7,8]
n=5
indice = Encontrar_Indice(lista,n)
print(indice)

