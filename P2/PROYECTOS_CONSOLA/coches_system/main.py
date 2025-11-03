from model import coches, cochesBD
import os

# Funciones de utilidad----------------------------------------------

def borrarPantalla():
    os.system("cls")

def esperaTecla():
    input("\n\t... Oprima una tecla para continuar ...")

#Funciones de negocio------------------------------------------------

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    while True:
        try:
            velocidad = int(input("Velocidad: "))
            break
        except ValueError:
            print("Velocidad debe ser un número entero.")
    while True:
        try:
            potencia = int(input("Potencia: "))
            break
        except ValueError:
            print("Potencia debe ser un número entero.")
    while True:
        try:
            plazas = int(input("No. de plazas: "))
            break
        except ValueError:
            print("No. de plazas debe ser un número entero.")
    return marca, color, modelo, velocidad, potencia, plazas

def imprimir_datos_vehiculo(marca, color, modelo, velocidad, potencia, plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def resultados_sql(respuesta):
    if respuesta:
        print("\n\tAccion realizada correctamente")
    else:
        print("No fue posible realizar la accion, intenta lo nuevamente ...")

def autos():
    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Auto")
    coche = coches.Coches(marca, color, modelo, velocidad, potencia, plazas)
    imprimir_datos_vehiculo(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)
    auto = cochesBD.Autos(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)
    respuesta = auto.insertar()
    if respuesta:
        print("Registro insertado correctamente")
    else:
        print("No fue posible insertar el registro, intenta lo nuevamente ...")
    esperaTecla()

def camionetas():
    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camioneta")
    traccion = input("Traccion: ").upper()
    cerrada = input("¿Cerrada (Si/No)?: ").upper().strip()
    cerrada = True if cerrada == "SI" else False
    coche = coches.Camionetas(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)
    imprimir_datos_vehiculo(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
    camioneta_bd = cochesBD.Camionetas(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas, coche.traccion, coche.cerrada)
    respuesta = camioneta_bd.insertar()
    if respuesta:
        print("Registro insertado correctamente")
    else:
        print("No fue posible insertar el registro, intentalo nuevamente ...")

def camiones():
    marca, color, modelo, velocidad, potencia, plazas = datos_autos("Camion")
    while True:
        try:
            eje = int(input("No. de ejes: "))
            break
        except ValueError:
            print("No. de ejes debe ser un número entero.")
    while True:
        try:
            capacidadCarga = int(input("Capacidad de carga (Kg): "))
            break
        except ValueError:
            print("Capacidad de carga debe ser un número entero.")
    coche = coches.Camiones(marca, color, modelo, velocidad, potencia, plazas, eje, capacidadCarga)
    imprimir_datos_vehiculo(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)
    print(f"No. de ejes: {coche.eje}\n Capacidad de carga (Kg): {coche.capacidadCarga}")
    camion_bd = cochesBD.Camiones(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas, coche.eje, coche.capacidadCarga)
    respuesta = camion_bd.insertar()
    if respuesta:
        print("Registro insertado correctamente")
    else:
        print("No fue posible insertar el registro, intentalo nuevamente ...")

def menu_acciones(tipo):
    print(f"\n\t\t ::: Menu de {tipo} ::.\n\t1.- Insertar\n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar")
    opcion = input("\tElige una opción: ").upper().strip()
    return opcion

def menu_autos():
    while True:
        borrarPantalla()
        opcion=menu_acciones("Autos")
        if opcion =="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,caballaje,plazas=autos()
            #Agregar en la BD
            auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
            respuesta=auto.insertar()
            resultados_sql(respuesta)
            esperaTecla()
        elif opcion =="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registros = cochesBD.Autos.consultar()
            if len(registros)>0:
                print("\n\t\t ::: Lista de Autos ::.")
                for registro in registros:
                    print(f"\nId: {registro[0]} \n Marca:{registro[1]} \n color: {registro[2]} \n Modelo: {registro[3]} \n velocidad: {registro[4]} \n caballaje: {registro[5]} \n plazas: {registro[6]}")  
                esperaTecla()
            else:
                input("\n\tNo hay registros de autos ...")
        elif opcion =="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=input("\nIngresar el ID del auto Actualizar: ")

            esperaTecla()
        elif opcion =="4" or opcion=="ELIMINAR":
            print("\n\tEliminar Autos - En construcción ...")
            esperaTecla()
        elif opcion =="5" or opcion=="REGRESAR":
            break
        else:
            input("\n\tOpción inválida ... vuelva a intentarlo ... ")

def main():
    opcion = True
    while opcion:
        os.system("cls")
        opcion = input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
        match opcion:
            case "1":
                menu_autos()
                esperaTecla()
            case "2":
                camionetas()
                esperaTecla()
            case "3":
                camiones()
                esperaTecla()
            case "4":
                borrarPantalla()
                input("\n\t\tSalir del Sistema")
                opcion = False
            case _:
                input("\n\tOpcion invalida ... vuelva a intertarlo ... ")

if __name__ == "__main__":
    main()