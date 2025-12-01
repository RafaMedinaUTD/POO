from tkinter import *
from tkinter import messagebox
from controller import controlador

class View():

    # add simple session storage
    current_user_id = None
    current_nombre = None
    current_apellidos = None

    def __init__(self,ventana):
        ventana.title("Gestion de Notas")
        ventana.geometry("800x600")
        self.menu_interfaz(ventana)

    @staticmethod
    def set_usuario(usuario_id, nombre, apellidos):
        View.current_user_id = usuario_id
        View.current_nombre = nombre
        View.current_apellidos = apellidos

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_interfaz(ventana):

        View.borrarPantalla(ventana)

        lblTitulo=Label(ventana,text="Menu principal")
        lblTitulo.pack(pady=5)

        btnRegistro=Button(ventana,text="1.-Registro",command=lambda: View.menu_registrar(ventana))
        btnRegistro.pack(pady=5)

        btnLogin=Button(ventana,text="2.-Login",command=lambda: View.menu_login(ventana))
        btnLogin.pack(pady=5)

        btnSalir=Button(ventana,text="3.-Salir",command=ventana.quit)
        btnSalir.pack(pady=5)

    @staticmethod
    def menu_registrar(ventana):

        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Inicio de sesion")
        lblTitulo.pack(pady=5)

        nomb=StringVar()
        lblNomb=Label(ventana,text="Cual es tu nombre?")
        lblNomb.pack(pady=5)
        txtNomb=Entry(ventana,textvariable=nomb)
        txtNomb.focus()
        txtNomb.pack(pady=5)

        apelli=StringVar()
        lblApelli=Label(ventana,text="Cuales son tus apellidos?")
        lblApelli.pack(pady=5)
        txtApelli=Entry(ventana,textvariable=apelli)
        txtApelli.focus()
        txtApelli.pack(pady=5)

        email=StringVar()
        lblEmail=Label(ventana,text="Ingresa tu email:")
        lblEmail.pack(pady=5)
        txtEmail=Entry(ventana,textvariable=email)
        txtEmail.focus()
        txtEmail.pack(pady=5)

        passw=StringVar()
        lblPassw=Label(ventana,text="Ingresa tu contraseña")
        lblPassw.pack(pady=5)
        txtPassw=Entry(ventana,textvariable=passw)
        txtPassw.focus()
        txtPassw.pack(pady=5)

        btnRegistrar=Button(ventana,text="Registrar",
                            command=lambda: [controlador.Controlador.registrar(txtNomb.get(),txtApelli.get(),txtEmail.get(),txtPassw.get()), 
                            View.menu_notas(ventana)])
        btnRegistrar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_interfaz(ventana))
        btnVolver.pack(pady=5)

    @staticmethod
    def menu_login(ventana):

        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Registro del sistema")
        lblTitulo.pack(pady=5)

        email=StringVar()
        lblEmail=Label(ventana,text="Ingresa tu email:")
        lblEmail.pack(pady=5)
        txtEmail=Entry(ventana,textvariable=email)
        txtEmail.focus()
        txtEmail.pack(pady=5)

        passw=StringVar()
        lblPassw=Label(ventana,text="Ingresa tu contraseña")
        lblPassw.pack(pady=5)
        txtPassw=Entry(ventana,textvariable=passw)
        txtPassw.focus()
        txtPassw.pack(pady=5)

        btnEntrar=Button(ventana,text="Entrar",
                          command=lambda: controlador.Controlador.login(txtEmail.get(),txtPassw.get(),ventana))
        btnEntrar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_interfaz(ventana))
        btnVolver.pack(pady=5)

    @staticmethod
    def menu_notas(ventana, usuario_id, nombre, apellidos):
        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f".:: Bienvenido {nombre} {apellidos}, has iniciado sesion ::.")
        lblTitulo.pack(pady=5)

        btnCrear=Button(ventana,text="1.-Crear",command=lambda: View.crear_nota(ventana))
        btnCrear.pack(pady=5)

        btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: View.mostrar_notas(ventana))
        btnMostrar.pack(pady=5)

        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: View.cambiar_nota(ventana))
        btnCambiar.pack(pady=5)

        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: View.eliminar_nota(ventana))
        btnEliminar.pack(pady=5)

        btnRegresar=Button(ventana,text="5.-Regresar",command=lambda: View.menu_interfaz(ventana))
        btnRegresar.pack(pady=5)

    @staticmethod
    def crear_nota(ventana):
        
        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Crear nota")
        lblTitulo.pack(pady=5)

        lblTituloNota=Label(ventana, text="Titulo: ", justify="center")
        lblTituloNota.pack(pady=10)

        titulo=StringVar()
        txtTitulo=Entry(ventana,textvariable=titulo)
        txtTitulo.focus()
        txtTitulo.pack(pady=5)
        
        lblDescripcion=Label(ventana, text="Descripcion: ", justify="center")
        lblDescripcion.pack(pady=10)

        descripcion=StringVar()
        txtDescripcion=Entry(ventana,textvariable=descripcion)
        txtDescripcion.focus()
        txtDescripcion.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command=lambda: controlador.Controlador.crear_nota(id_user,txtTitulo.get(),txtDescripcion.get()))
        btnGuardar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btnVolver.pack(pady=5)

    @staticmethod
    def mostrar_notas(ventana):

        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, tus notas son: ",justify="center")
        lblTitulo.pack(pady=5)

        filas=""
        registros=controlador.Controlador.mostrar_nota(id_user)
        # registros=[("1","100","Nota 1", "Descripcion de la nota 1", "2025-11-24")]
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"Nota: {num_notas}\nTitulo: {fila[2]} - ID: {fila[0]}\n Fecha de Creacion: {fila[4]}\n Descripcion: {fila[3]}\n"
                num_notas+=1
        else:
            messagebox.showinfo(icon="info", message=".:: No existen notas para este usuario ::.")

        lblResultado=Label(ventana, text=filas)
        lblResultado.pack(pady=10)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btnVolver.pack(pady=5)

    @staticmethod
    def cambiar_nota(ventana):
            
        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, vamos a modificar una Nota")
        lblTitulo.pack(pady=5)

        lblID=Label(ventana, text="ID de la nota a cambiar: ", justify="center")
        lblID.pack(pady=10)

        idn=StringVar()
        txtID=Entry(ventana,textvariable=idn)
        txtID.focus()
        txtID.pack(pady=5)

        lblTituloNota=Label(ventana, text="Nuevo Titulo: ", justify="center")
        lblTituloNota.pack(pady=10)

        titulo=StringVar()
        txtTitulo=Entry(ventana,textvariable=titulo)
        txtTitulo.focus()
        txtTitulo.pack(pady=5)
            
        lblDescripcion=Label(ventana, text="Nueva Descripcion: ", justify="center")
        lblDescripcion.pack(pady=10)

        descripcion=StringVar()
        txtDescripcion=Entry(ventana,textvariable=descripcion)
        txtDescripcion.focus()
        txtDescripcion.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command=lambda: controlador.Controlador.cambiar_nota(txtID.get(),txtTitulo.get(),txtDescripcion.get()))
        btnGuardar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btnVolver.pack(pady=5)

    @staticmethod
    def eliminar_nota(ventana):
            
        View.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"{nom_user} {ape_user}, vamos a eliminar una Nota")
        lblTitulo.pack(pady=5)

        lblID=Label(ventana, text="ID de la nota a eliminar: ", justify="center")
        lblID.pack(pady=10)

        idn=StringVar()
        txtID=Entry(ventana,textvariable=idn)
        txtID.focus()
        txtID.pack(pady=5)

        btnEliminar=Button(ventana,text="Eliminar",command=lambda: controlador.Controlador.eliminar_nota(txtID.get()))
        btnEliminar.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btnVolver.pack(pady=5)