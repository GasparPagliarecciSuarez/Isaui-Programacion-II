peso = float(input("Ingrese su peso en KG por favor: "))
altura = float(input("Por favor ingrese su altura en metros, separado por un punto" ))
if  altura > 2.30 : 
    altura = altura / 100
else:    altura = altura
imc = peso / altura ** 2
print("Su IMC es de: " + str(round(imc, 2)))