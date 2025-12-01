from tkinter import messagebox
from model import operaciones
class Controladores():
    @staticmethod
    def operacion(a,b,op,caracter):
        match op:
            case "suma":
                opera=a+b
                
            case "resta":
                opera=a-b
            case "multiplicacion":
                opera=a*b
            case "division":
                opera=a/b
        messagebox.showinfo(message=f"El resultado de {a} {caracter} {b} es: {opera}",title=op)
        respuesta=messagebox.askquestion(message=f"Quieres insertarlo en la base de datos").lower()
        if respuesta=="yes":
            operaciones.Operaciones.crear(a,b,caracter,opera)
        else:
            pass

    @staticmethod
    def buscar(id):
        dato=operaciones.Operaciones.obtener_por_id(id)
        if dato:
            messagebox.showinfo(message=f"Operacion encontrada:\nID: {dato[0]}\nNumero 1: {dato[2]}\nNumero 2: {dato[3]}\nSigno: {dato[4]}\nResultado: {dato[5]}",title="Busqueda Exitosa")
        else:
            messagebox.showerror(message="No se encontro la operacion con el ID proporcionado",title="Error de Busqueda")
    
    @staticmethod
    def eliminar(id):
        respuesta=messagebox.askquestion(message=f"Deseas eliminar la operacion con ID: {id} de la base de datos?",icon="warning").lower()
        if respuesta=="yes":
            operaciones.Operaciones.eliminar(id)
            Controladores.respuesta_sql("Eliminacion",True)
        else:
            pass

    @staticmethod
    def mostrar():
        datos=operaciones.Operaciones.mostrar()
        return datos
    
    def cambiar(numero1,numero2,signo,resultado,id):
        respuesta=messagebox.askquestion(message=f"Deseas Cambiar la operacion en la base de datos?",icon="warning").lower()
        if respuesta=="yes":
            operaciones.Operaciones.cambiar(numero1,numero2,signo,resultado,id)
        else:
            pass
    

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(message=f"{titulo} realizada con exito",icon="info")
        else:
            messagebox.showerror(message=f"Error al realizar la {titulo}",icon="error")