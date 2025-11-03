from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Marcos o Frame en Tkinter")
#Ventana.resizable(False,False)#no puede modificarse el tamaño de la ventana

marco1=Frame(ventana,width=400,height=200,bg="blue",border=10,relief=SOLID)
marco1.pack() #Es importante para que se dibuje o muestre el widget o el objeto entro de la ventana
marco2=Frame(marco1,width=300,height=150,bg="silver",relief=GROOVE,border=10).pack()



ventana.mainloop()