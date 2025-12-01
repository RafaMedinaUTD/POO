"""
  Crear una calculadora:
  1.- Dos campos de Texto
  2.- 4 botones para las Operaciones
  3.- Mostrar el Resultado en una alerta
"""
from tkinter import messagebox
from tkinter import *
from view import interfaz

def operaciones(titulo,numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="x":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}{signo}{numero2}={resultado}")

# def mensaje(titulo,numero1,numero2,resultado):
#     messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}+{numero2}={resultado}")

# #Controlador o Controller
# def suma(numero1,numero2):
#     sumar=numero1+numero2
#     mensaje("Sumar",numero1,numero2,sumar)

# def resta(numero1,numero2):
#     restar=numero1-numero2
#     mensaje("Restar",numero1,numero2,restar)

# def multiplicacion(numero1,numero2):
#     multi=numero1*numero2
#     mensaje("Multiplicación",numero1,numero2,multi)

# def division(numero1,numero2):
#     dividir=numero1/numero2
#     mensaje("Dividir",numero1,numero2,dividir)
