#Calculadora promedio 3 num
print("Para calcular el promedio entre 3 números siga las siguientes intrucciones")
num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
num3= float(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3
promedio = suma / 3

print ("El promedio es de " + str (round(promedio,2)))