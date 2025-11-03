from tkinter import *
ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso del mainloop")

marco1=Frame(ventana,width=600,height=66.66666,bg="#ff3c00",border=2,relief=RAISED)
marco1.pack()
marco2=Frame(ventana,width=600,height=66.66666,bg="#FF9900",border=2,relief="raised")
marco2.pack()
marco3=Frame(ventana,width=600,height=66.66666,bg="#FBFF00",border=2,relief=RAISED)
marco3.pack()
marco4=Frame(ventana,width=600,height=66.66666,bg="#00A51B",border=2,relief=RAISED)
marco4.pack()
marco5=Frame(ventana,width=600,height=66.66666,bg="#4400FF",border=2,relief=RAISED)
marco5.pack()
marco6=Frame(ventana,width=600,height=66.66666,bg="#9D00AC",border=2,relief=RAISED)
marco6.pack()

ventana.mainloop()