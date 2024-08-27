
import tkinter 

ventana= tkinter.Tk()
ventana.geometry("300x100")
ventana.title("sumar restar y resetear")


def aumentar():
    suma= int(Entry_1.get())
    nuevo_valor= suma +1
    Entry_1_var.set(nuevo_valor)

def disminuir():
    suma= int(Entry_1.get())
    nuevo_valor= suma -1
    Entry_1_var.set(nuevo_valor)
def reset():
    Entry_1_var.set(0)


label_1= tkinter.Label(ventana, text="Contador")
label_1.grid(row=0,column=0, padx=5,pady=5)

button_1 = tkinter.Button(ventana, text="+",command=aumentar)
button_1.grid(row=0,column=2, padx=5,pady=5)

button_2 = tkinter.Button(ventana, text="-",command=disminuir)
button_2.grid(row=0,column=3, padx=5,pady=5)

button_3 = tkinter.Button(ventana, text="reset",command=reset)
button_3.grid(row=0,column=4, padx=5,pady=5)

Entry_1_var= tkinter.StringVar(value=0)
Entry_1=tkinter.Entry(ventana, textvariable=(Entry_1_var),state="readonly",justify="center")
Entry_1.grid(row=0, column=1, columnspan=1, padx=5,pady=5)




ventana.mainloop()