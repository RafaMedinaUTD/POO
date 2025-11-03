from tkinter import *
import webbrowser


ventana = Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("400x400")
ventana.config(
    bg="lightblue"
)


def saludar():
    usuario=entry1.get()
    contrasena=entry2.get()

    label2.config(text=f"Hola bienvenido {usuario}")
    if usuario=="" or contrasena=="":
        label2.config(text=f"Existen Campos Vacios, Por favor ingrese algo...")

def borrar():
    entry1.delete(0,END)
    entry2.delete(0,END)
    label2.config(text=f"")

label1=Label(ventana,text="Acceso al sistema:")
label1.config(
    bg="#1fc2df",
    border="10",
    width=40,
    height=1,
    relief=GROOVE

)
label1.pack()


label2=Label(ventana,text="Usuario:",bg="lightblue")
label2.pack()

usuario=StringVar()
entry1=Entry(ventana, width="50")
entry1.pack()


label3=Label(ventana,text="Contraseña:",bg="lightblue")
label3.pack()

contrasena=StringVar()
entry2=Entry(ventana, width="50")
entry2.pack()

button1=Button(ventana,text="Iniciar Sesion",command=saludar)
button1.pack()

label2=Label(ventana,text="",bg="lightblue")
label2.pack()

btn_borrar=Button(ventana,text="Borrar Campos",command=borrar)
btn_borrar.pack()

ventana.mainloop() 
