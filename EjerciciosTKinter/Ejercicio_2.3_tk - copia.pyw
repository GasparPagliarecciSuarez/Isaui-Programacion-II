import tkinter
import random 
ventana= tkinter.Tk()

ventana.geometry("400x150") 
ventana.title('Aleatorio')
ventana.resizable(0,0)


def aleatorio():
    r1=int(spnbox_1.get())
    r2=int(spnbox_2.get())
    if r1>r2:
        modal= tkinter.Toplevel(ventana)
        modal.geometry("280x100")
        modal.title('Error')
        modal.resizable(0,0)

        error=tkinter.Label(modal,text="El primer numero no puede ser mayor al segundo")
        error.pack(pady=20)

   
        close_button = tkinter.Button(modal, text="Cerrar", command=modal.destroy)
        close_button.pack(pady=5)
        


    else:
        Resultado = int(random.randint(r1,r2))
    entry_var.set(Resultado)
   
   


lbl_1= tkinter.Label(ventana, text="Numero 1 ")
lbl_1.grid(column=0,row=0,padx=50)

lbl_2= tkinter.Label(ventana, text="Numero 2",padx=50)
lbl_2.grid(column=0,row=1,pady=10)

lbl_3= tkinter.Label(ventana, text="Numero generado ")
lbl_3.grid(column=0,row=2,padx=50)

spnbox_1_var=tkinter.IntVar(value=1)
spnbox_1=tkinter.Spinbox(ventana,from_=1, to =20,textvariable=spnbox_1_var)
spnbox_1.grid(column=1,row=0)

spnbox_2_var=tkinter.IntVar(value=1)
spnbox_2=tkinter.Spinbox(ventana,from_=1, to =20,textvariable=spnbox_2_var)
spnbox_2.grid(column=1,row=1)


entry_var=tkinter.StringVar(value='')
entry=tkinter.Entry(ventana,textvariable=entry_var,state="readonly")
entry.grid(column=1,row=2)


bttn= tkinter.Button(ventana,text="Agregar",command=aleatorio)
bttn.grid(column=1,row=3)



ventana.mainloop()