from tkinter import messagebox
from model import usuario,nota
from view import vista

class Controlador:

    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info", message=f"{nombre} {apellidos}, se registro correctamente con el email: {email}")
        else:
            messagebox.showinfo(icon="warning", message=f"{nombre} {apellidos}, no se pudo completar el proceso, intentelo nuevamente")
    
    @staticmethod
    def login(email,password,ventana):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info", message=f"{registro[1]} {registro[2]}, haz iniciado sesion correctamente.")
            vista.View.set_usuario(registro[0], registro[1], registro[2])
            vista.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
            messagebox.showinfo(icon="warning", message=f"Credenciales incorrectas, intentelo nuevamente")
    
    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        resultado=usuario.Usuario.crear_nota(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Notas",resultado)
    
    @staticmethod
    def mostrar_nota(usuario_id):
        notas=usuario.Usuario.mostrar_nota(usuario_id)
        return notas
    
    @staticmethod
    def eliminar_nota(id):
        resultado=usuario.Usuario.eliminar_nota(id)
        Controlador.respuesta_sql("Eliminar Nota",resultado)
    
    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        resultado=usuario.Usuario.cambiar_nota(id,titulo,descripcion)
        Controlador.respuesta_sql("Cambiar Nota",resultado)

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo, message=f"Accion realizada correctamente")
        else:
            messagebox.showinfo(icon="warning",title=titulo, message=f"No se pudo completar la accion, intentelo nuevamente")