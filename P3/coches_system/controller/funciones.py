from model.coches import Coches, Camionetas, Camiones
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
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            camioneta = Camionetas(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            cursor.execute(
                "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (camioneta.marca, camioneta.color, camioneta.modelo, camioneta.velocidad, camioneta.caballaje, camioneta.plazas, camioneta.traccion, camioneta.cerrada)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, toneladas):
        try:
            camion = Camiones(marca, color, modelo, velocidad, caballaje, plazas, toneladas)
            cursor.execute(
                "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, toneladas) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (camion.marca, camion.color, camion.modelo, camion.velocidad, camion.caballaje, camion.plazas, camion.toneladas)
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
    def consultar_camionetas():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def consultar_camiones():
        try:
            cursor.execute("SELECT * FROM camiones")
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
    def consultar_camioneta_por_id(id_camioneta):
        try:
            cursor.execute("SELECT * FROM camionetas WHERE id=%s", (id_camioneta,))
            return cursor.fetchone()
        except:
            return None

    @staticmethod
    def consultar_camion_por_id(id_camion):
        try:
            cursor.execute("SELECT * FROM camiones WHERE id=%s", (id_camion,))
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
    def actualizar_camioneta(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute(
                "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s",
                (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def actualizar_camion(id_camion, marca, color, modelo, velocidad, caballaje, plazas, toneladas):
        try:
            cursor.execute(
                "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, toneladas=%s WHERE id=%s",
                (marca, color, modelo, velocidad, caballaje, plazas, toneladas, id_camion)
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
    def eliminar_camioneta(id_camioneta):
        try:
            cursor.execute("DELETE FROM camionetas WHERE id=%s", (id_camioneta,))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar_camion(id_camion):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s", (id_camion,))
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