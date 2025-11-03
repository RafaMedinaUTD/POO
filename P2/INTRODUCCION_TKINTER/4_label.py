from tkinter import *
ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso de etiquetas")

marco1=Frame(ventana,width=600,height=100,bg="#00ff9d",border=2,relief=GROOVE)
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana,width=600,height=100,bg="#6FE9FF",border=2,relief=GROOVE)
marco2.pack_propagate(False)
marco2.pack()
marco3=Frame(ventana,width=600,height=100,bg="#8805AF",border=2,relief=GROOVE)
marco3.pack_propagate(False)
marco3.pack()
marco4=Frame(ventana,width=600,height=100,bg="#FA3889",border=2,relief=GROOVE)
marco4.pack_propagate(False)
marco4.pack()

#Etiquetas o Label

Etiqueta1=Label(marco1,text="Rafael Abraham Castañeda Medina",bg="#00ff9d",fg="black",font=("Papyrus",16,"bold","italic"))
Etiqueta1.pack(pady=30) 
Etiqueta2=Label(marco2,text="Universidad Tecnologica de Durango",bg="#6FE9FF",fg="black",font=("Arial",16))
Etiqueta2.pack(pady=30) 
Etiqueta3=Label(marco3,text="Tecnologias de la infiormación",bg="#8805AF",fg="black",font=("Calibri",16))
Etiqueta3.pack(pady=30) 
Etiqueta4=Label(marco4,text="Desarrollo de SW Multiplataforma",bg="#FA3889",fg="black",font=("Times New Roman",16))
Etiqueta4.pack(pady=30) 

ventana.mainloop()