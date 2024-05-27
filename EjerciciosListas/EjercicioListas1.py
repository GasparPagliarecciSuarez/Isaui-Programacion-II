def SUMA_ELEMENTOS(lista):
    
    suma=0
    cont = 0
    while cont < len(lista):
        suma += lista[cont]
        cont += 1
    return suma


entrada = input('Ingrese una lista de números que desee sumar (Separados por comas): ')
lista= [int(x) for x in entrada.split(',')]
suma = SUMA_ELEMENTOS(lista)

print ('La suma de sus números es de:' , suma)