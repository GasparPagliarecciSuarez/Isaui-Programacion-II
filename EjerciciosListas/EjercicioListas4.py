def MAYOR_QUE_N (lista):
    n = int(input("Ingrese el numero para realizar la comparasion "))
    cont = 0
    listaMayor=[]
    while cont<len(lista):
        if lista[cont]>n:
            listaMayor.append(lista[cont])
        cont +=1
    return sorted(listaMayor)

entrada = input('Ingrese una lista de números separados por comas: ')
lista= [int(x) for x in entrada.split(',')]
listaMayor1 = MAYOR_QUE_N(lista)
print ("los números mayores al ingresado son:",listaMayor1)


