
import re
contador = 0 
contraseña = input("Por favor ingrese una contraseña de al menos 8 caracteres, que incluya : \n una letra minuscula \n una letra mayuscula \n un número \n un caracter especial \n Contraseña: ")
if len(contraseña) >= 8 :
    contador = contador +1 

if re.search(r'[a-z]', contraseña):
    contador = contador +1 

if re.search(r'[A-Z]', contraseña):
    contador = contador +1 

if re.search(r'[0-9]', contraseña):
    contador = contador +1 

if re.search(r'[!@#$%^&*+_]', contraseña):
    contador = contador +1 

if re.search(r'[a-z]', contraseña):
    contador = contador +1 


if contador == 6:
    print("Su contraseña es correcta")

else:
    print("Su contraseña no cumple con los estandares requeridos, por favor intente nuevamente con las instrucciones dadas")