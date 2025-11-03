from tkinter import *
ventana=Tk()
ventana.geometry("600x500")
ventana.title("Uso de botones, marcos y etiquetas")

def cambiarTexto():
    Etiqueta2.config(text="Dag fiscal")
    Etiqueta3.config(text="123")
def regresarTexto():
    Etiqueta2.config(text="Usuario:...")
    Etiqueta3.config(text="Contraseña:...")


marco1=Frame(ventana,width=600,height=100,bg="#00ff9d",border=2,relief=GROOVE)
marco1.pack_propagate(False)
marco1.pack()


#Etiquetas o Label

Etiqueta1=Label(marco1,text="Inicio de Sesion",bg="#00ff9d",fg="black",font=("Papyrus",16,"bold","italic"))
Etiqueta1.pack(pady=30) 
Etiqueta2=Label(text="Usuario: ...",fg="black",font=("Arial",16))
Etiqueta2.pack(pady=30) 
Etiqueta3=Label(text="Contraseña:...",fg="black",font=("Calibri",16))
Etiqueta3.pack(pady=30) 


Boton1=Button(text="Entrar",fg="black",font=("Times New Roman",16),command=cambiarTexto)
Boton1.pack(pady=30) 
Boton2=Button(text="Regresar",fg="black",font=("Times New Roman",16),command=regresarTexto)
Boton2.pack(pady=30) 

ventana.mainloop()