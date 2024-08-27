import tkinter

ventana= tkinter.Tk()

ventana.geometry("500x300") 
ventana.title('Peliculas')
ventana.resizable(0,0)

def agregar():

    pelicula = entry_var.get()
    

    if pelicula in lista1.get(0,tkinter.END):
            modal= tkinter.Toplevel(ventana)
            modal.geometry("200x100")
            modal.title('Error')
            modal.resizable(0,0)

            error=tkinter.Label(modal,text="La pelicula ya ha sido agregada")
            error.pack(pady=20)

   
            close_button = tkinter.Button(modal, text="Cerrar", command=modal.destroy)
            close_button.pack(pady=5)
    else: lista1.insert(tkinter.END,pelicula)


    entry_var.set("")
    
   


lbl_1= tkinter.Label(ventana, text="Ingrese su pelicula")
lbl_1.grid(column=0,row=0,padx=50)

lbl_2= tkinter.Label(ventana, text="lista de peliculas",padx=50)
lbl_2.grid(column=1,row=0,pady=10)


entry_var=tkinter.StringVar(value='')
entry=tkinter.Entry(ventana,textvariable=entry_var)
entry.grid(column=0,row=1)


bttn= tkinter.Button(ventana,text="Agregar",command=agregar)
bttn.grid(column=0,row=2)


lista1= tkinter.Listbox (ventana)
lista1.grid(column=1,row=1)

ventana.mainloop()