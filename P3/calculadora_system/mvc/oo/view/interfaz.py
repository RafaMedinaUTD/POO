from tkinter import *
from controller import funciones
from model import operaciones

class Vistas():
    def __init__(self,ventana):
        ventana.geometry("600x600")
        ventana.title("Calculadora")
        ventana.resizable(False,False)
        self.interfaz(ventana)

    def menuPrincipal(self, ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        operacionesMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)

        operacionesMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        operacionesMenu.add_command(label="Consultar",command=lambda: self.mostrarOperaciones(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda: self.cambiarOperacion(ventana))
        operacionesMenu.add_command(label="Borrar",command=lambda: self.eliminar(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)


    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        num1=IntVar()
        txtNum1=Entry(ventana,textvariable=num1,justify=CENTER,width=10)
        txtNum1.focus()
        txtNum1.pack()
        num2=IntVar()
        txtNum2=Entry(ventana,textvariable=num2,justify=CENTER,width=10)
        txtNum2.pack(pady=20)

        btnSuma=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"suma","+"),text="+ SUMA",border=4,relief=RAISED)
        btnSuma.pack()

        btnResta=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"resta","-"),text="- RESTA",border=4,relief=RAISED)
        btnResta.pack()

        btnMulti=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"multiplicacion","X"),text="* MULTIPLICACION",border=4,relief=RAISED)
        btnMulti.pack()

        btnDivision=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"division","/"),text="/ DIVISION",border=4,relief=RAISED)
        btnDivision.pack()

        btnSalir=Button(ventana,command=ventana.quit,text="Salir",border=4,relief=RAISED,background="#DA6868",activebackground="#810404")
        btnSalir.pack(pady=30)

    def eliminar(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar una Operación ::.",justify=CENTER)
        lbl_titulo.pack(pady=10)
        lbl_info=Label(ventana,text="Ingrese el ID de la Operación a eliminar",justify=CENTER)
        lbl_info.pack(pady=10)
        id=IntVar()
        txtID=Entry(ventana,textvariable=id,justify=CENTER,width=10)
        txtID.focus()
        txtID.pack()
        btnBuscar=Button(ventana,text="Buscar",command=lambda: funciones.Controladores.buscar(id.get()), border=4,relief=RIDGE,background="#DA6868",activebackground="#810404")
        btnBuscar.pack(pady=10)
        btnVolver=Button(ventana,command=lambda: self.interfaz(ventana),text="Volver",border=4,relief=RAISED,background="#DA6868",activebackground="#810404")
        btnVolver.pack(pady=30)
        
#self.eliminarbusqueda(ventana,id)


    def eliminarbusqueda(self, ventana, id):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=".:: Eliminar una Operación ::.",justify=CENTER)
        lbl_titulo.pack(pady=10)
        lbl_info=Label(ventana,text=f"ID de la Operación",justify=CENTER)
        lbl_info.pack(pady=10)

        txtID=Entry(ventana,justify=CENTER,width=10)
        txtID.insert(0, id.get())
        txtID.config(state="readonly")
        txtID.pack()

        btnEliminar=Button(ventana,text="Eliminar",command=lambda: funciones.Controladores.eliminar(id.get()), border=4,relief=RIDGE,background="#DA6868",activebackground="#810404")
        btnEliminar.pack(pady=10)
        btnVolver=Button(ventana,command=lambda: self.interfaz(ventana),text="Volver",border=4,relief=RAISED,background="#DA6868",activebackground="#810404")
        btnVolver.pack(pady=30)
        
    
    def mostrarOperaciones(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        datos=funciones.Controladores.mostrar()
        lbl_titulo=Label(ventana,text=".:: Listado de las Operaciones ::.",justify=CENTER)
        lbl_titulo.pack(pady=10)

        texto=""
        for fila in datos:
            texto+=f"Operacion: {fila[0]} ID: {fila[0]} Fecha de Creacion: {fila[1]} \n Operación: {fila[2]} {fila[4]} {fila[3]} = {fila[5]}\n"

        lbl_datos=Label(ventana,text=texto,justify=CENTER)
        lbl_datos.pack(pady=10)

        btnVolver=Button(ventana,command=lambda: self.interfaz(ventana),text="Volver",border=4,relief=RAISED,background="#DA6868",activebackground="#810404")
        btnVolver.pack(pady=30)
    
    def cambiarOperacion(self, ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lbl_titulo=Label(ventana,text=".:: Cambiar una Operación ::.",justify=CENTER)
        lbl_titulo.pack(pady=10)
        lbl_id=Label(ventana,text="ID de la operacion",justify=CENTER)
        lbl_id.pack(pady=10)
        id=IntVar()
        txtID=Entry(ventana,textvariable=id,justify=CENTER,width=10)
        txtID.focus()
        txtID.pack()
        lbl_num1=Label(ventana,text="Nuevo Numero 1",justify=CENTER)
        lbl_num1.pack(pady=10)
        numero1=IntVar()
        txtNum1=Entry(ventana,textvariable=numero1,justify=CENTER,width=10)
        txtNum1.pack()
        lbl_num2=Label(ventana,text="Nuevo Numero 2",justify=CENTER)
        lbl_num2.pack(pady=10)
        numero2=IntVar()
        txtNum2=Entry(ventana,textvariable=numero2,justify=CENTER,width=10)
        txtNum2.pack()
        lbl_signo=Label(ventana,text="Nuevo Signo",justify=CENTER)
        lbl_signo.pack(pady=10)
        signo=StringVar()
        txtSigno=Entry(ventana,textvariable=signo,justify=CENTER,width=10)
        txtSigno.pack()
        lbl_resultado=Label(ventana,text="Nuevo Resultado",justify=CENTER)
        lbl_resultado.pack(pady=10)
        resultado=IntVar()
        txtResultado=Entry(ventana,textvariable=resultado,justify=CENTER,width=10)
        txtResultado.pack()
        btnCambiar=Button(ventana,text="Guardar",command=lambda:funciones.Controladores.cambiar(numero1.get(),numero2.get(),signo.get(),resultado.get(),txtID.get()), border=4,relief=RAISED,background="#7FC755",activebackground="#048143")
        btnCambiar.pack(pady=30)
        btnVolver=Button(ventana,command=lambda: self.interfaz(ventana),text="Volver",border=4,relief=RAISED,background="#DA6868",activebackground="#810404")
        btnVolver.pack(pady=10)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()