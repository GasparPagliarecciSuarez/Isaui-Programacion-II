#Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y los valores son listas de sus calificaciones. 
#La función debe devolver un nuevo diccionario con las mismas claves pero donde los valores son la calificación promedio de cada estudiante.

def Promedios_Notas(diccionario):
    diccionario_Promedios={}
    for a, b in diccionario.items():
        b = sum (b) / len (b)
        diccionario_Promedios[a] = b

    return diccionario_Promedios

diccionario = {

        'Lola': [6,4,4,6,9,7],
        'German':[5,4,7,7,6],
        'Felix':[5,3,3,1,4],
        'Spiderman': [10,10,10,10,10]
                 }

diccionarioPromedios= Promedios_Notas(diccionario)
print ("Notas alumnos de los alumnos:", diccionario)
print ("Promedio de notas los alumnos:",diccionarioPromedios)
