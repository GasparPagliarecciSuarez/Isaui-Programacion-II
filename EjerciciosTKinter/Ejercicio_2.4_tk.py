
import tkinter 

ventana= tkinter.Tk()
ventana.geometry("350x200")
ventana.title("calculadora")
ventana.resizable (False,False)



def calcular():
    try:
        n1=float(Entry_1_var.get())
        n2= float(Entry_2_var.get())
    except ValueError:
            modal= tkinter.Toplevel(ventana)
            modal.geometry("200x100")
            modal.title('Error')
            modal.resizable(0,0)

            error=tkinter.Label(modal,text="No puedes ingresar letras")
            error.pack(pady=20)

   
            close_button = tkinter.Button(modal, text="Cerrar", command=modal.destroy)
            close_button.pack(pady=5)

            Entry_1_var.set('')
            Entry_2_var.set('')

                 
            n1 = float(Entry_1_var.get())
            n2 = float(Entry_2_var.get())
            resultado = float(n1 + n2)
            
    n1 = float(Entry_1_var.get())
    n2 = float(Entry_2_var.get())
    operacion = opcion_var.get()

    if operacion=="sumar":
        
        resultado = float(n1 + n2)

           
    if operacion=="restar":
    
        resultado = float(n1 - n2)


    if operacion== 'multiplicar':
    
        resultado = float(n1 * n2)



    if operacion=="dividir":
        resultado = float(n1 / n2)


  
    if operacion=='porcentaje':
        resultado = float(n1 * n2 / 100)


    Entry_3_var.set(round(resultado,4))
  
def clear():
    Entry_1_var.set(0)
    Entry_2_var.set(0)
    Entry_3_var.set(0)



opcion_var=tkinter.StringVar(value='')



label_1= tkinter.Label(ventana, text="primer num")
label_1.grid(row=0,column=0, padx=5,pady=5)

label_2= tkinter.Label(ventana, text="segundo num")
label_2.grid(row=1,column=0, padx=5,pady=5)


label_3= tkinter.Label(ventana, text="resultado")
label_3.grid(row=2,column=0, padx=5,pady=5)

label_4=tkinter.Label(ventana,text="Operaciones")
label_4.grid(row=0,column=3, padx=5,pady=5)


button_1 = tkinter.Button(ventana, text="Calcular",command=calcular)
button_1.grid(row=4,column=2)


rdbttn_1=tkinter.Radiobutton(ventana,text='sumar',variable=opcion_var,value="sumar")
rdbttn_1.grid(row=1,column=3, padx=5,pady=5)

rdbttn_2=tkinter.Radiobutton(ventana,text='restar',variable=opcion_var,value="restar")
rdbttn_2.grid(row=2,column=3, padx=5,pady=5)

rdbttn_3=tkinter.Radiobutton(ventana,text='multiplicar',variable=opcion_var,value="multiplicar")
rdbttn_3.grid(row=3,column=3, padx=5,pady=5)

rdbttn_4=tkinter.Radiobutton(ventana,text='dividir',variable=opcion_var,value="dividir")
rdbttn_4.grid(row=4,column=3, padx=5,pady=5)



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