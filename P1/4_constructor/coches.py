import os
os.system("cls")

#Metodo Constructor.- Con este metodo se inicializa un objeto cuando es creado con valores iniciales
class Coches():
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas


 

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
coche1=Coches("VW,","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)



print(f"Las marca del Coche 1 son: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

print(f"Las marca del Coche 2 son: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlazas: {coche2.getPlazas()}")

