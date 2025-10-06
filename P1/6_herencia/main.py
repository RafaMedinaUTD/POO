
import os
#Instanciar los objetos para posterior implementarlos
from coches import Coches,Camionetas,Camiones


os.system("cls")
coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca, coche.acelerar())
    
camioneta=Camionetas("Chevrolet","Rojo","2021",180,150,5,"4x4",False)
print(camioneta.marca, camioneta.acelerar())

camion=Camiones("Volvo","Azul","2019",140,400,3,4,10000)
print(camion.marca, camion.acelerar())

# num_coche=int(input("Cuantos coches desea ingresar: "))
# for i in range(0,num_coche):
#     print(f"\n\t ..::Datos del Coche {i+1}::..")
#     marca=input("Ingrese la marca del coche: ").upper()
#     color=input("Ingrese el color del coche: ").upper()
#     modelo=input("Ingrese el modelo del coche: ").upper()
#     velocidad=int(input("Ingrese la velocidad del coche: "))
#     caballaje=int(input("Ingrese el caballaje del coche: "))
#     plazas=int(input("Ingrese las plazas del coche: "))

# coche1=Coches(marca,color,modelo,velocidad,caballaje,plazas)

# print(f"Las marca del Coche 1 son: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

# print(f"\n{coche1.acelerar()}")
