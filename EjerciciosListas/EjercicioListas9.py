#Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.
def Producto_De_Elementos(lista):
    listaProd=[]
    cont = 0
    suma = 0
    for elemento in lista:
        if cont == 0:
            resultado = elemento * lista[cont]
            cont+=1
        else: 
            resultado = resultado * lista [cont]
            cont +=1
        suma = resultado

    listaProd=suma
    return listaProd

lista=[2,3,4]
#Hace 2*2 = 4   4*3 = 12   12 * 4 =  48

listaProd=Producto_De_Elementos(lista)
print(listaProd)