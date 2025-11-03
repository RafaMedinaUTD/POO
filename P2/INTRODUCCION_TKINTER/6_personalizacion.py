from tkinter import *


ventana=Tk()


ventana.title("Personalizar Widgets u Objetos")
ventana.geometry("500x600")



def cambiarLabel():
    etiqueta.config(
        text="POO con python",
        bg="green",
        fg="black",
        width=50,
        height=4,
        font=("Helvetica",30,"italic"),
        relief=SOLID,
        border=2
    )
def regresarLabel():
    etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    border=2,
    text="Bienvenidos a Tkinter"
)


etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    border=2
)
etiqueta.pack(pady=25)

boton1=Button(ventana,text="Haz click ...",command=cambiarLabel)
boton1.config(
    fg="black",
    bg="white",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="white",
    activebackground="black",
    cursor="target"
    )
boton1.pack(pady=30)

boton2=Button(ventana,text="Regresar ...",command=regresarLabel)
boton2.config(
    fg="white",
    bg="black",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="black",
    activebackground="white",
    cursor="target"
    )
boton2.pack(pady=30)



ventana.mainloop()