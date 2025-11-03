from tkinter import *
import webbrowser


ventana = Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("800x600")

def saludar():
    label2.config(text=f"Hola bienvenido {entry1.get()}")
    if entry1.get()=="claudia sheinbaum":
        label2.config(text=f"Chinga tu madre {entry1.get()}")
    if entry1.get()=="alex":
        label2.config(text=f"{entry1.get()} es jotinchon")
    if entry1.get()=="friv":
        webbrowser.open_new("www.friv.com")

label1=Label(ventana,text="Ingrese su nombre:")
label1.pack()

entry1=Entry(ventana, width="50")
entry1.pack()

button1=Button(ventana,text="Saludar",command=saludar)
button1.pack()

label2=Label(ventana,text="")
label2.pack()

ventana.mainloop() 
