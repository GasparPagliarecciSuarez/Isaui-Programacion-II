def CALCULAR_MAX_MIN(lista):
    ListaORD= sorted(lista)
    max=ListaORD[-1]
    min=ListaORD[0]
    
    return print("El valor maximo es:",max,"\nEl valor mínimo es:", min)
    
entrada = input('Ingrese una lista de números separados por comas: ')
lista= [int(x) for x in entrada.split(',')]
maxmin = CALCULAR_MAX_MIN(lista)
