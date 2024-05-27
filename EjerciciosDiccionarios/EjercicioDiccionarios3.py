def Merge_Diccionarios(Dic1, Dic2):
    diccionario_Combinado = {}
    diccionario_Combinado = Dic1.copy()
    diccionario_Combinado.update(Dic2)
    return print ("El nuevo diccionario combinado es: ", diccionario_Combinado)
    
Dic1 = {}
Dic2 = {}
while True:
        
        clave = input("Ingrese la clave para el primer diccionario: ")
        if clave.lower() == 'fin':
            break
        valor = input("Ingrese el valor: ")
        if valor.lower() == 'fin':
            break
        Dic1[clave]=valor
        print (Dic1)
while True:
        
        clave = input("Ingrese la clave para el segundo diccionario: ")
        if clave.lower() == 'fin':
            break
        valor = input("Ingrese el valor: ")
        if valor.lower() == 'fin':
            break
        Dic2[clave]=valor
        print (Dic2)

Dic3 = {}
Dic3 = Merge_Diccionarios (Dic1,Dic2)
