'''

Ejercicio Práctico #2 "Modelar y Diagramar en POO"

'''
import os

os.system("cls")

#Clase de Coches
class Coches:
    #Método constructor (Inicializa los valores cuando se instancia un objeto de la clase)
    def __init__(self, color, marca, velocidad): 
        self.__color = color #Atributos del objeto
        self.__marca = marca
        self.__velocidad = velocidad

    #Métodos del objeto
    def acelerar(self, incremento):
        self.__velocidad = self.__velocidad + incremento
        return self.__velocidad
    
    def frenar(self, decremento):
        self.__velocidad = self.__velocidad - decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("Pip pip")

#Instanciar objetos de la clase coches
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)

print(coche1.acelerar(50))
print(coche2.frenar(100))
print(coche1.tocar_claxon())

# print(f"Los valores del objeto 1 son: {coche1.marca}, {coche1.color}, {coche1.velocidad}")
# print(f"El coche 1 acelero de: {coche1.velocidad} a {coche1.acelerar(50)} ")
# print(f"Los valores del objeto 2 son: {coche2.marca}, {coche2.color}, {coche2.velocidad}")
# print(f"El coche 2 freno de: {coche2.velocidad} a {coche2.frenar(100)} ")