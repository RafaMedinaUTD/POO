import os
os.system("cls")

class Coches():
    __marca = ""
    __color = ""
    __modelo = ""
    __velocidad = 0
    __caballaje = 0
    __plazas = 0

#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto
#En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
#Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

#1er forma de crear los metodos getters y setters
    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

#2da forma de crear los metodos getters y setters
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def getCaballaje(self):
        return self.__caballaje

    def setCaballaje(self, caballaje):
        self.__caballaje = caballaje

    def getPlazas(self):
        return self.__plazas

    def setPlazas(self, plazas):
        self.__plazas = plazas

#Metodos o acciones o funciones que hace el objeto

def acelerar(self,incremento):
        pass

def frenar(self,decremento):
        pass

#Multiples Objetos
coche1=Coches()
coche2=Coches()
coche3=Coches()

coche1.setMarca("Nissan")
coche1.setColor("Azul")
coche1.setModelo("2020")
coche1.setVelocidad(180)
coche1.setCaballaje(150)
coche1.setPlazas(6)
coche1.num_serie="1200971624"

coche2.setMarca("VW")
coche2.setColor("Blanco")
coche2.setModelo("2022")
coche2.setVelocidad(220)
coche2.setCaballaje(150)
coche2.setPlazas(5)

coche3.marca="Honda"

print(f"Las marca del Coche 1 son: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

print(f"Las marca del Coche 2 son: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlazas: {coche2.getPlazas()}")

print(f"La marca del Coche 3 es: {coche3.marca}")