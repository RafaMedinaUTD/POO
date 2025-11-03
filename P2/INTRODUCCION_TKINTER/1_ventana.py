"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""
from tkinter import *

# import tkinter as hola
# ventana = hola.Tk()

ventana = Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("800x600")

ventana.mainloop() #Metodo que permite tener la ventana abierta todo el tiempo que dure la app activa
