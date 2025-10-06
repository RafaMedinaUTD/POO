#Encapsular .- Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una clase a la hora de usar en objetos o en herencia
import os 
os.system("cls")

class Clase:
    atributo_publico = "Soy un atributo publico"
    _atributo_protegido = "Soy un atributo protegido"
    __atributo_privado = "Soy un atributo privado"

    def __init__(self, color, tamanio):
        self.__color = color
        self.__tamanio = tamanio

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    @property
    def atributopublico(self):
        return self.__class__.atributo_publico
    @atributopublico.setter
    def atributo_publico(self, atributo):
        self.__class__.atributo_publico = atributo
    
    @property
    def _atributo_protegido(self):
        return self.__class__._atributo_protegido
    @_atributo_protegido.setter
    def _atributo_protegido(self, atributo):
        self.__class__._atributo_protegido = atributo
    
    @property
    def atributoPrivado(self):
        return self.__atributo_privado
    @atributoPrivado.setter
    def atributoPrivado(self, atributo):
        self.__atributo_privado = atributo
    

#Utilizar la clase

objeto = Clase("Rojo", "Grande")
print(objeto.color, objeto.tamanio)
#print(objeto.publico) No es una buena practica acceder directamente a los atributos
print(objeto.atributo_publico)
print(objeto._atributo_protegido)
print(objeto.atributoPrivado) 