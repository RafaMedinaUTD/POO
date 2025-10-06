import os
os.system("cls")

class Coches():
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    def acelerar(self,incremento):
        pass

    def frenar(self,decremento):
        pass
coche1=Coches()
coche2=Coches()

coche1.marca="Nissan"
coche1.color="Azul"
coche1.modelo="2020"
coche1.velocidad=180
coche1.caballaje=150
coche1.plazas=6

print(f"Las marca del Coche 1 son: \nMarca: {coche1.marca} \nColor: {coche1.color} \nModelo{coche1.modelo} \nVelocidad: {coche1.velocidad}, \nCaballaje: {coche1.caballaje} \nPlazas: {coche1.plazas}")

coche2 = Coches()
coche2.marca = "VW"
coche2.color = "Blanco"
coche2.modelo = "2022" 
coche2.velocidad = 220
coche2.caballaje = 150
coche2.plazas = 5

print(f"Las marca del Coche 2 son: \nMarca: {coche2.marca} \nColor: {coche2.color} \nModelo{coche2.modelo} \nVelocidad: {coche2.velocidad} \nCaballaje: {coche2.caballaje} \nPlazas: {coche2.plazas}")