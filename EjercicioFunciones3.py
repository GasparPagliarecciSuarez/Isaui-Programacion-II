def CALCULAR_AREA_PERIMETRO(circunferencia):

    radio = circunferencia/2
    pi=3.1416

    perimetro= pi * circunferencia
    area= pi * (radio * radio)

    return print("El area de su circulo es de:", round(area,2), "Centimetros ","\nEl perimetro de su circulo es de:", round(perimetro,2), "Centimetros ")

circulo = int(input("Para conocer el area y perimetro, ingrese el diametro de su circulo en CM \n(El resultado obtenido sera expresado en la misma unidad) :"))
CALCULAR_AREA_PERIMETRO(circulo)

