import os
"""
Practica # 1 Implementar paradigma estructurado VS OO
Crear un programa que obtenga el area de un rectangulo
"""

#1.-Estructurado
# def area_rectangulo():
#     os.system("cls")
#     base=float(input(f"Base del Rectangulo: \t"))
#     altura=float(input(f"Altura del Rectangulo: \t"))
#     area=base*altura
#     print(f"El area del rectangulo es igual a: {area}")
# area_rectangulo()

#2.-OO

class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def areaRectangulo(self):
        os.system("cls")
        area=self.base*self.altura
        return area

rectangulo=AreaRectangulo(5,6) #instanciar un objeto de la clase "AreaRectangulo"

print(f"El area del rectangulo es: {rectangulo.areaRectangulo(5,6)}")