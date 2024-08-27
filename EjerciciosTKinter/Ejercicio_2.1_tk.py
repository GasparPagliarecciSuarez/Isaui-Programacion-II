
import tkinter 

ventana= tkinter.Tk()
ventana.geometry("250x200")
ventana.title("calculadora")
ventana.resizable (False,False)

def sumar():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    resultado = float(n1 + n2)


    Entry_3_var.set(resultado)
    return resultado


def restar():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    resultado = float(n1 - n2)


    Entry_3_var.set(resultado)
    return resultado
    

def multiplicar():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    resultado = float(n1 * n2)


    Entry_3_var.set(resultado)
    return resultado

def dividir():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    resultado = float(n1 / n2)


    Entry_3_var.set(resultado)
    return resultado

def porcentaje():
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    resultado = float(n1 * n2 / 100)


    Entry_3_var.set(resultado)
    return resultado

def clear():
    Entry_1_var.set(0)
    Entry_2_var.set(0)
    Entry_3_var.set(0)



label_1= tkinter.Label(ventana, text="primer num")
label_1.grid(row=0,column=0, padx=5,pady=5)

label_2= tkinter.Label(ventana, text="segundo num")
label_2.grid(row=1,column=0, padx=5,pady=5)


label_3= tkinter.Label(ventana, text="resultado")
label_3.grid(row=2,column=0, padx=5,pady=5)


button_1 = tkinter.Button(ventana, text="+",command=sumar)
button_1.grid(row=3,column=0, padx=5,pady=5)

button_2 = tkinter.Button(ventana, text="-",command=restar)
button_2.grid(row=3,column=1,padx=2,pady=2)

button_3 = tkinter.Button(ventana, text="*",command= multiplicar)
button_3.grid(row=3,column=2, padx=2,pady=2)

button_4 = tkinter.Button(ventana, text="/", command= dividir)
button_4.grid(row=4,column=0, padx=2,pady=2)

button_5 = tkinter.Button(ventana, text="%",command=porcentaje)
button_5.grid(row=4,column=1,padx=2,pady=2)

button_6 = tkinter.Button(ventana, text="C", command=clear)
button_6.grid(row=4,column=2, padx=2,pady=2)


Entry_1_var= tkinter.StringVar(value=0)
Entry_1=tkinter.Entry(ventana, textvariable=(Entry_1_var),justify="center")
Entry_1.grid(row=0, column=2, columnspan=1, padx=5,pady=5)

Entry_2_var= tkinter.StringVar(value=0)
Entry_2=tkinter.Entry(ventana, textvariable=(Entry_2_var),justify="center")
Entry_2.grid(row=1, column=2, columnspan=1, padx=5,pady=5)

Entry_3_var= tkinter.StringVar(value=0)
Entry_3=tkinter.Entry(ventana, textvariable=(Entry_3_var),state="readonly",justify="center")
Entry_3.grid(row=2, column=2, columnspan=1, padx=5,pady=5)


ventana.mainloop()