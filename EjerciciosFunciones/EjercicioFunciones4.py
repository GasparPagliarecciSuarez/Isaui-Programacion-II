def VALIDAR_USUARIO(usario,contraseña):
    intentos = 0
    while intentos<3:
        if usario != "usuario1" or contraseña != "asdasd":
            print("El usuario o contraseña ingresados no es correcto")    
            intentos += 1

            if intentos < 3 :
                usario = input("Ingrese su usuario nuevamente: ")
                contraseña = input("Ingrese su contraseña nuevamente: ")
        else:
            print("Usted a ingresado correctamente")
            break
        if intentos== 3:
            print ("Usted a superado el número máximo de intentos permitidos. Contactese con el soporte para tramitar el recupero de su cuenta")
            break

usuario = input("Ingrese su usuario: ")
contraseña1 = input("Ingrese su contraseña: ")
VALIDAR_USUARIO(usuario,contraseña1)