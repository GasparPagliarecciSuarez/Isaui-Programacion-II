
import tkinter 

ventana= tkinter.Tk()
ventana.geometry("500x100")
ventana.title("calculadora de factoriales")


def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_factorial( ):
    global n
    n+=1
    Entry_1_var.set(n)
    fact= factorial(n)
    Entry_2_var.set(fact)

n=1

label_1= tkinter.Label(ventana, text="n")
label_1.grid(row=0,column=0, padx=5,pady=5)

label_2= tkinter.Label(ventana, text="(n)")
label_2.grid(row=0,column=2, padx=5,pady=5)

button_1 = tkinter.Button(ventana, text="siguiente",command=calcular_factorial)
button_1.grid(row=0,column=4,columnspan=3, padx=5,pady=5)

Entry_1_var= tkinter.StringVar(value=1)
Entry_1=tkinter.Entry(ventana, textvariable=(Entry_1_var),state="readonly",justify="center")
Entry_1.grid(row=0, column=1, columnspan=1, padx=5,pady=5)

Entry_2_var= tkinter.StringVar(value=factorial(n))
Entry_2=tkinter.Entry(ventana, textvariable=(Entry_2_var),state="readonly",justify="center")
Entry_2.grid(row=0, column=3, columnspan=1, padx=5,pady=5)



ventana.mainloop()