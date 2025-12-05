from model.coches import Coches
from conexionBD import conexion, cursor
from tkinter import messagebox

class ControladorAutos:
    def __init__(self):
        pass

    @staticmethod
    def insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            auto = Coches(marca, color, modelo, velocidad, caballaje, plazas)
            cursor.execute(
                "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)",
                (auto.marca, auto.color, auto.modelo, auto.velocidad, auto.caballaje, auto.plazas)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar_autos():
        try:
            cursor.execute("SELECT * FROM autos")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def consultar_auto_por_id(id_auto):
        try:
            cursor.execute("SELECT * FROM autos WHERE id=%s", (id_auto,))
            return cursor.fetchone()
        except:
            return None

    @staticmethod
    def actualizar_auto(id_auto, marca, color, modelo, velocidad, caballaje, plazas):
        try:
            cursor.execute(
                "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s",
                (marca, color, modelo, velocidad, caballaje, plazas, id_auto)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar_auto(id_auto):
        try:
            cursor.execute("DELETE FROM autos WHERE id=%s", (id_auto,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def respuesta_operacion(titulo, exito):
        if exito:
            messagebox.showinfo(titulo, "Operación realizada correctamente")
            
        else:
            messagebox.showerror(titulo, "Error al realizar la operación")
    
def crear_coche(datos):

    return "menu_acciones"  

def actualizar_coche(datos):

    return "menu_acciones"

def eliminar_coche(id_coche):

    return "menu_acciones"