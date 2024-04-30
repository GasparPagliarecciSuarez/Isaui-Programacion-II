while True:
    valor = int(input("Seleccione a que medida de temperatura desea convertir: 1) Farenheit, 2) celcius: "))
    #valor = input()
    if valor == 2:
        Grados = float(input("Por favor ingrese la temperatura en grados farenheit: "))
        conversion = (Grados - 32) * 5 / 9 
        print ("Los grados celsius son:" + str (round(conversion,1)))
        break
    if valor ==1:
        Grados = float(input("Por favor ingrese la temperatura en grados Celcius: "))
        conversion = (Grados * 1.8) + 32 
        print ("Los grados Farenheit son:" + str (round(conversion,1)))
        break
    if valor !=1 and valor != 2:
        print ("Por favor Ingrese un número correcto para continuar con la conversión")
    