import os
from coches import *

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("Oprima una tecla para continuar...")

def imprimirDatos(marca,color,modelo,velocidad,caballaje,plazas):
    print(f"Los datos del Vehiculo son:\nMarca: {marca} \nColor: {color} \nModelo: {modelo} \nVelocidad: {velocidad} \nCaballaje: {caballaje} \nPlazas: {plazas}")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ... Ingresar los datos del Vehiculo de tipo: {tipo} ...")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    caballaje=int(input("Caballaje: "))
    plazas=int(input("Plazas: "))
    return marca,color,modelo,velocidad,caballaje,plazas

def autos():
    borrarPantalla()
    print(f"\n\t ..::Datos del Vehiculo::..")
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Auto")

    coche=Coches(marca,color,modelo,velocidad,caballaje,plazas)

    imprimirDatos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

def camionetas():
    borrarPantalla()
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada? (Si/No): ")
    if cerrada.lower()=="si":
        cerrada=True
    else:
        cerrada=False

    coche=Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    imprimirDatos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\nTraccion: {coche.traccion} \nCerrada: {coche.cerrada}")

def camiones():
    borrarPantalla()
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
    imprimirDatos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\nEjes: {coche.eje} \nCapacidad de Carga: {coche.capacidadCarga}")
    
def main():
    opcion=True
    while opcion:
        borrarPantalla()

        print("\n\t\t..::Menu Principal::.. \n1.- Autos \n2.- Camionetas \n3.- Camiones\n4.- Salir")
        opcion=input("Ingrese una opcion: ").lower().strip()
        match opcion:
            case"1":
                borrarPantalla()
                print("Autos")
                autos()
                espereTecla()
            case"2":
                borrarPantalla()
                print("Camionetas")
                camionetas()
                espereTecla()
            case"3":
                borrarPantalla()
                print("Camiones")
                camiones()
                espereTecla()
            case"4":
                borrarPantalla()
                print(f"\n\tGracias por su visita")
                espereTecla()
                opcion=False
            case _:
                print(f"\n\tOpcion incorrecta, intente de nuevo")
                espereTecla()

if __name__=="__main__":
    main()