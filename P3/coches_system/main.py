from view.interfaz import InterfazAutos
from controller.funciones import ControladorAutos

if __name__ == "__main__":
    controlador = ControladorAutos()
    app = InterfazAutos(controlador)
    app.ejecutar()