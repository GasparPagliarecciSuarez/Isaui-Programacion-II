def Concatenar_Listas(lista1,lista2):
    nuevaLista=[]
    nuevaLista= lista1 + lista2

    return nuevaLista


lista1= [1,2,3,4]
lista2= ["a","b",'c','d']
nuevaLista = Concatenar_Listas(lista1,lista2)
print (nuevaLista)