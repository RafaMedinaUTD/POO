import os
os.system("cls")


class Profesores():
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
        def impartir(self):
            pass
        def evaluar(self):
            pass

class Alumnos():
    def __init__(self, nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

class Cursos():
    def __init__(self, nombre, codigo, creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos
        def asignar(self):
            pass
        

#Profesores----------------------------------------------
def getNombre(self):
    return self.__nombre
def setNombre(self, nombre):
    self.__nombre = nombre

def getExperiencia(self):
    return self.__experiencia
def setExperiencia(self, experiencia):
    self.__experiencia = experiencia

def getNum_profesor(self):
    return self.__num_profesor
def setNum_profesor(self, num_profesor):
    self.__num_profesor = num_profesor

#Alumnos----------------------------------------------
def getNombre(self):
    return self.__nombre
def setNombre(self, nombre):
    self.__nombre = nombre

def getEdad(self):
    return self.__edad
def setEdad(self, edad):
    self.__edad = edad

def getMatricula(self):
    return self.__matricula
def setMatricula(self, matricula):
    self.__matricula = matricula

#Cursos----------------------------------------------
def getNombre(self):
    return self.__nombre
def setNombre(self, nombre):
    self.__nombre = nombre

def getCodigo(self):
    return self.__codigo
def setCodigo(self, codigo):
    self.__codigo = codigo

def getCreditos(self):
    return self.__creditos
def setCreditos(self, creditos):
    self.__creditos = creditos


#Profesores------------------------------
profesor1=Profesores("Ana Torres Guzman", 40, "123")
profesor2=Profesores("Daniel Contreras", 35, "124")

#Cursos------------------------------
curso1=Cursos("POO", "100", 6)
curso2=Cursos("FOSO", "100", 4)

#Alumnos------------------------------
alumno1=Alumnos("Juan Correa Simental", 25, "100123")
alumno2=Alumnos("Maria Serrano Mata", 22, "100124")

print(f"El alumno {alumno1._Alumnos__nombre} se ha inscrito al curso de {curso1._Cursos__nombre} impartido por la profesora {profesor1._Profesores__nombre}")

print(f"El alumno {alumno2._Alumnos__nombre} se ha inscrito al curso de {curso2._Cursos__nombre} impartido por el profesor {profesor2._Profesores__nombre}")