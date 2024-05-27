#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def Contar_Elementos(lista,valor):
    resultado = 0
    cont = 0
    for elemento in lista:
        if elemento == valor:
            cont +=1
            

    resultado = cont
    return resultado

lista=[1,2,3,3,3,3,3,4,4,3]
n = 4
resultado = Contar_Elementos(lista,n)
print(resultado) 