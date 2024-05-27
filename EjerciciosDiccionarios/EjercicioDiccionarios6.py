#Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
#intercambie los valores de esas dos claves en el diccionario.

def Intercambiar_Valores(dicc,clave1,clave2):
    
    if clave1 and clave2 in dicc:
        copia_clave1= dicc[clave1]
        dicc[clave1] = dicc[clave2]
        dicc[clave2] = copia_clave1
    return dicc

diccionario = {
        "a":1,
        "b":"Tiene que ser C",
        "c":'Tiene que ser B',
        "d":4,
        "e":5,

}
clave1="b"
clave2="c"

diccinvert=Intercambiar_Valores(diccionario,clave1,clave2)
print(diccinvert)