import tkinter 
import random

ventana= tkinter.Tk()
ventana.geometry("600x400")
ventana.title("calculadora")
ventana.resizable (False,False)

juegos = 0
buenos = 0
malos = 0
opcion_varDif=tkinter.StringVar(value='')
dificultad = opcion_varDif.get()
r1 = 0
r2 = 0


class LCDNumber:
    def __init__(self, master):
        self.master = master
        self.master.title("Contador LCD")
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        
        self.time_left = 60  # Tiempo inicial en segundos
        

def aleatorios():
    global juegos, r1, r2
    dificultad = opcion_varDif.get()
    if dificultad == "facil":
        r1=1
        r2=10
    if dificultad == "medio":
        r1=1
        r2=100
    if dificultad == "dificil":
        r1=0
        r2=1000
    Entry_1_var.set(random.randint(r1,r2))
    Entry_2_var.set(random.randint(r1,r2))
    radbuttn=random.randint(1,4)
    opcion_var.set(radbuttn)
    juegos+=1
    label_5_var.set(juegos)

    if radbuttn == 1:
        label_1_var.set('+')

    if radbuttn == 2:
        label_1_var.set('-')

    if radbuttn == 3:
        label_1_var.set('x')
    
    if radbuttn == 4:
        label_1_var.set('/')

    

def calcular():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    operacion = opcion_var.get()
    
   

    if operacion=="1":
        label_1_var.set('+')
        resultado = float(n1 + n2)

           
    if operacion=="2":
        label_1_var.set('-')
        resultado = float(n1 - n2)


    if operacion== '3':
        label_1_var.set('*')
        resultado = float(n1 * n2)



    if operacion=="4":
        label_1_var.set('/')
        resultado = float(n1 / n2)

    
    return resultado

#Entry_3_var.set(round(resultado,4))
def comparar():
    global juegos, buenos, malos
    calculado = calcular()
    entrada_usuario = float(Entry_3_var.get())
    
    
    if calculado == entrada_usuario:
        #Entry_4_var.set("Correcto")
        buenos+=1
        label_6_var.set(buenos)
        Entry_1_var.set(0)
        Entry_2_var.set(0)
        Entry_3_var.set(0)

        
        
        
    else:
        #Entry_4_var.set("Incorrecto")
        malos+=1
        label_7_var.set(malos)
        Entry_1_var.set(0)
        Entry_2_var.set(0)
        Entry_3_var.set(0)
        
def clear():
    Entry_1_var.set(0)
    Entry_2_var.set(0)
    Entry_3_var.set(0)



opcion_var=tkinter.StringVar(value='')


label_1_var=tkinter.StringVar(value="")
label_1= tkinter.Label(ventana, textvariable=label_1_var)
label_1.grid(row=0,column=1, padx=5,pady=5)

label_2= tkinter.Label(ventana, text="Juegos:")
label_2.grid(row=5,column=3, padx=5,pady=5)

label_3= tkinter.Label(ventana, text="Buenos:")
label_3.grid(row=6,column=3, padx=5,pady=5)

label_4= tkinter.Label(ventana, text="Malos:")
label_4.grid(row=7,column=3, padx=5,pady=5)

label_5_var=tkinter.StringVar(value="")
label_5= tkinter.Label(ventana, textvariable=label_5_var)
label_5.grid(row=5,column=4, padx=5,pady=5)

label_6_var=tkinter.StringVar(value="")
label_6= tkinter.Label(ventana, textvariable=label_6_var)
label_6.grid(row=6,column=4, padx=5,pady=5)

label_7_var=tkinter.StringVar(value="")
label_7= tkinter.Label(ventana, textvariable=label_7_var)
label_7.grid(row=7,column=4, padx=5,pady=5)






button_1 = tkinter.Button(ventana, text="Resultado",command=comparar)
button_1.grid(row=4,column=3)

#BOTON PARA COMPARAR USADO DURANTE EL DESARROLLO
'''button_3 = tkinter.Button(ventana, text="comparar",command=comparar)
button_3.grid(row=4,column=4)'''

button_2 = tkinter.Button(ventana, text="Nuevo Numero",command=aleatorios)
button_2.grid(row=1,column=3)


rdbttn_1=tkinter.Radiobutton(ventana,text='sumar',variable=opcion_var,value="1",state="disabled")
rdbttn_1.grid(row=1,column=0, padx=5,pady=5)

rdbttn_2=tkinter.Radiobutton(ventana,text='restar',variable=opcion_var,value="2",state="disabled")
rdbttn_2.grid(row=2,column=0, padx=5,pady=5)

rdbttn_3=tkinter.Radiobutton(ventana,text='multiplicar',variable=opcion_var,value="3",state="disabled")
rdbttn_3.grid(row=3,column=0, padx=5,pady=5)

rdbttn_4=tkinter.Radiobutton(ventana,text='dividir',variable=opcion_var,value="4",state="disabled")
rdbttn_4.grid(row=4,column=0, padx=5,pady=5)

rdbttn_5=tkinter.Radiobutton(ventana,text='facil',variable=opcion_varDif,value="facil")
rdbttn_5.grid(row=8,column=1, padx=5,pady=5)

rdbttn_6=tkinter.Radiobutton(ventana,text='medio',variable=opcion_varDif,value="medio")
rdbttn_6.grid(row=8,column=2, padx=5,pady=5)

rdbttn_7=tkinter.Radiobutton(ventana,text='dificil',variable=opcion_varDif,value="dificil")
rdbttn_7.grid(row=8,column=3, padx=5,pady=5)




Entry_1_var= tkinter.StringVar(value=0)
Entry_1=tkinter.Entry(ventana, textvariable=(Entry_1_var),justify="center",state="readonly")
Entry_1.grid(row=0, column=0, columnspan=1, padx=5,pady=5)

Entry_2_var= tkinter.StringVar(value=0)
Entry_2=tkinter.Entry(ventana, textvariable=(Entry_2_var),justify="center",state="readonly")
Entry_2.grid(row=0, column=2, columnspan=1, padx=5,pady=5)

Entry_3_var= tkinter.StringVar(value=0)
Entry_3=tkinter.Entry(ventana, textvariable=(Entry_3_var),justify="center")
Entry_3.grid(row=3, column=3, columnspan=1, padx=5,pady=5)

#Entry_4_var= tkinter.StringVar(value=0)
#Entry_4=tkinter.Entry(ventana, textvariable=(Entry_4_var),justify="center")
#Entry_4.grid(row=6, column=6, columnspan=1, padx=5,pady=5)


ventana.mainloop()