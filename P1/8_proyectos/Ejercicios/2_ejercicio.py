'''
#Prueba
# class Calculadora():
#     def __init__ (self,entero1,entero2):
#         self._entero1=entero1
#         self._entero2=entero2

# def ingreso(self):
#     calculadora.entero1=int(input("Ingrese el primer numero entero: "))
#     calculadora.entero2=int(input("Ingrese el segundo numero entero: "))

# def sumar(resultado):
#     resultado=(calculadora.entero1+calculadora.entero2)
#     print(f"La suma de {calculadora.entero1} + {calculadora.entero2} es: {resultado}")
#     return resultado

# def restar(resultado):
#     resultado=(calculadora.entero1-calculadora.entero2)
#     print(f"La resta de {calculadora.entero1} - {calculadora.entero2} es: {resultado}")
#     return resultado

# def multi(resultado):
#     resultado=(calculadora.entero1*calculadora.entero2)
#     print(f"La multiplicacion de {calculadora.entero1} * {calculadora.entero2} es: {resultado}")
#     return resultado

# def division(resultado):
#     resultado=(calculadora.entero1/calculadora.entero2)
#     print(f"La division de {calculadora.entero1} / {calculadora.entero2} es: {resultado}")
#     return resultado
'''
import os
os.system("cls")

class Calculadora():
    def __init__ (self):
        self._numero1=int(input("Numero 1: "))
        self._numero2=int(input("Numero 2: "))
    
    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self, numero1):
        self._numero1 = numero1

    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2

    def sumar(self):
        return self._numero1 + self._numero2
    
    def restar(self):
        return self._numero1 - self._numero2
    
    def multiplicar(self):
        return self._numero1 * self._numero2
    
    def dividir(self):
        return self._numero1 / self._numero2
    
operacion=Calculadora()
print(f"{operacion.numero1} + {operacion.numero2} = {operacion.sumar()}")
print(f"{operacion.numero1} - {operacion.numero2} = {operacion.restar()}")
print(f"{operacion.numero1} * {operacion.numero2} = {operacion.multiplicar()}")
print(f"{operacion.numero1} / {operacion.numero2} = {operacion.dividir()}")