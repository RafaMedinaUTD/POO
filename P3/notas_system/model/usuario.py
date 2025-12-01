
from conexionBD import *
import hashlib
import datetime


class Usuario:
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        try:
            
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellidos,email,hashlib.sha256(password.encode()).hexdigest(),fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
          return None         
    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into notas values(null,%s,%s,%s,%s)",
                (usuario_id,titulo,descripcion,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def mostrar_nota(usuario_id):
        try:
            cursor.execute(
                "select * from notas where usuario_id=%s",
                (usuario_id,)
            )
            notas=cursor.fetchall()
            return notas
        except:    
          return []
    @staticmethod
    def eliminar_nota(id):
        try:
            cursor.execute(
                "delete from notas where id=%s",
                (id,)
            ) 
            conexion.commit() 
            return True  
        except:    
          return False
    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        try:
            cursor.execute(
                "update notas set titulo=%s, descripcion=%s where id=%s",
                (titulo,descripcion,id)
            ) 
            conexion.commit() 
            return True  
        except:    
          return False