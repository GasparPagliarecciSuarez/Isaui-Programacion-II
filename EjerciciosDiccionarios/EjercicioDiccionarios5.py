#Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
#diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def Calcular_Cuadrados_Hasta_n(n):
    dicc = {}
    n = 6
    cont = 1
    
    while cont<= n:
        cuadrados = cont * cont
        dicc[cont] = cuadrados
        cont +=1
    return print (dicc)

n=6
dicc = {}
dicc = Calcular_Cuadrados_Hasta_n(n)

