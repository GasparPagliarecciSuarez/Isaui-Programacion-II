def Promedio(lista):
    cont = 0
    suma = 0
    while cont < len(lista):
        suma += lista[cont]
        cont +=1
    Promedio = suma / len(lista)
    return print("El promedio de la lista es de: ", Promedio)
    
entrada = input('Ingrese una lista de números separados por comas: ')
lista= [int(x) for x in entrada.split(',')]
Prom = Promedio(lista)


#tenor-ezgif.com-gif-maker.gif