import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

class InterfazAutos:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Sistema de Coches")
        self.root.geometry("700x500")
    
    def borrarPantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def menu_principal(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="SISTEMA DE GESTIÓN DE COCHES", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="AUTOS", command=self.menu_acciones_coches, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CAMIONETAS", command=self.menu_acciones_camionetas, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CAMIONES", command=self.menu_acciones_camiones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="SALIR", command=self.root.quit, width=20, height=2).pack(pady=10)
        
    def menu_acciones_coches(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="GESTIÓN DE AUTOS", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="INSERTAR", command=self.insertar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CONSULTAR", command=self.consultar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ACTUALIZAR", command=self.cambiar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ELIMINAR", command=self.borrar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_principal, width=20, height=2).pack(pady=10)

    def menu_acciones_camionetas(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="GESTIÓN DE CAMIONETAS", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="INSERTAR", command=self.insertar_camionetas, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CONSULTAR", command=self.consultar_camionetas, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ACTUALIZAR", command=self.cambiar_camionetas, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ELIMINAR", command=self.borrar_camionetas, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_principal, width=20, height=2).pack(pady=10)

    def menu_acciones_camiones(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="GESTIÓN DE CAMIONES", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="INSERTAR", command=self.insertar_camiones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CONSULTAR", command=self.consultar_camiones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ACTUALIZAR", command=self.cambiar_camiones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ELIMINAR", command=self.borrar_camiones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_principal, width=20, height=2).pack(pady=10)
        
    def insertar_autos(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="INSERTAR NUEVO AUTO", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="Marca:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_marca_auto = tk.Entry(frame_form, width=30)
        self.entry_marca_auto.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Color:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_color_auto = tk.Entry(frame_form, width=30)
        self.entry_color_auto.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_modelo_auto = tk.Entry(frame_form, width=30)
        self.entry_modelo_auto.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Velocidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_velocidad_auto = tk.Entry(frame_form, width=30)
        self.entry_velocidad_auto.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Caballaje:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_caballaje_auto = tk.Entry(frame_form, width=30)
        self.entry_caballaje_auto.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Plazas:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_plazas_auto = tk.Entry(frame_form, width=30)
        self.entry_plazas_auto.grid(row=5, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="GUARDAR", command=self.guardar_auto, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_coches, width=15).pack(side="left", padx=10)
        
    def guardar_auto(self):
        marca = self.entry_marca_auto.get()
        color = self.entry_color_auto.get()
        modelo = self.entry_modelo_auto.get()
        velocidad = self.entry_velocidad_auto.get()
        caballaje = self.entry_caballaje_auto.get()
        plazas = self.entry_plazas_auto.get()
        
        if not all([marca, color, modelo, velocidad, caballaje, plazas]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
            
        messagebox.showinfo("Éxito", "Auto guardado correctamente")
        
    def insertar_camionetas(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="INSERTAR NUEVA CAMIONETA", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="Marca:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_marca_camioneta = tk.Entry(frame_form, width=30)
        self.entry_marca_camioneta.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Color:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_color_camioneta = tk.Entry(frame_form, width=30)
        self.entry_color_camioneta.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_modelo_camioneta = tk.Entry(frame_form, width=30)
        self.entry_modelo_camioneta.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Velocidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_velocidad_camioneta = tk.Entry(frame_form, width=30)
        self.entry_velocidad_camioneta.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Caballaje:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_caballaje_camioneta = tk.Entry(frame_form, width=30)
        self.entry_caballaje_camioneta.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Plazas:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_plazas_camioneta = tk.Entry(frame_form, width=30)
        self.entry_plazas_camioneta.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Tracción:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_traccion_camioneta = tk.Entry(frame_form, width=30)
        self.entry_traccion_camioneta.grid(row=6, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Cerrada (Si/No):").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.entry_cerrada_camioneta = tk.Entry(frame_form, width=30)
        self.entry_cerrada_camioneta.grid(row=7, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="GUARDAR", command=self.guardar_camioneta, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_camionetas, width=15).pack(side="left", padx=10)
        
    def guardar_camioneta(self):
        messagebox.showinfo("Éxito", "Camioneta guardada correctamente")
        
    def insertar_camiones(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="INSERTAR NUEVO CAMIÓN", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="Marca:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_marca_camion = tk.Entry(frame_form, width=30)
        self.entry_marca_camion.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Color:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_color_camion = tk.Entry(frame_form, width=30)
        self.entry_color_camion.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_modelo_camion = tk.Entry(frame_form, width=30)
        self.entry_modelo_camion.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Velocidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_velocidad_camion = tk.Entry(frame_form, width=30)
        self.entry_velocidad_camion.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Caballaje:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_caballaje_camion = tk.Entry(frame_form, width=30)
        self.entry_caballaje_camion.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Plazas:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_plazas_camion = tk.Entry(frame_form, width=30)
        self.entry_plazas_camion.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="No. de Ejes:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_ejes_camion = tk.Entry(frame_form, width=30)
        self.entry_ejes_camion.grid(row=6, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Capacidad de Carga:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.entry_capacidad_camion = tk.Entry(frame_form, width=30)
        self.entry_capacidad_camion.grid(row=7, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="GUARDAR", command=self.guardar_camion, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_camiones, width=15).pack(side="left", padx=10)
        
    def guardar_camion(self):
        messagebox.showinfo("Éxito", "Camión guardado correctamente")
        
    def consultar_autos(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="CONSULTAR AUTOS REGISTRADOS", font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_coches, width=20).pack(pady=20)

    def consultar_camionetas(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="CONSULTAR CAMIONETAS REGISTRADAS", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_camionetas, width=20).pack(pady=20)

    def consultar_camiones(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="CONSULTAR CAMIONES REGISTRADOS", font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_camiones, width=20).pack(pady=20)
        
    def cambiar_autos(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ACTUALIZAR AUTO", font=("Arial", 16)).pack(pady=20)
        
        frame_buscar = tk.Frame(self.root)
        frame_buscar.pack(pady=10)
        
        tk.Label(frame_buscar, text="ID del auto a actualizar:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id_actualizar_auto = tk.Entry(frame_buscar, width=20)
        self.entry_id_actualizar_auto.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(frame_buscar, text="BUSCAR", command=self.buscar_auto_actualizar, width=10).grid(row=0, column=2, padx=10, pady=5)
        
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_coches, width=20).pack(pady=20)
        
    def buscar_auto_actualizar(self):
        id_auto = self.entry_id_actualizar_auto.get()
        if not id_auto:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        self.mostrar_formulario_actualizar_auto(id_auto)
    
    def mostrar_formulario_actualizar_auto(self, id_auto):
        self.borrarPantalla()
        
        tk.Label(self.root, text=f"ACTUALIZAR AUTO - ID: {id_auto}", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="Marca:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_marca = tk.Entry(frame_form, width=30)
        entry_marca.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Color:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_color = tk.Entry(frame_form, width=30)
        entry_color.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_modelo = tk.Entry(frame_form, width=30)
        entry_modelo.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Velocidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_velocidad = tk.Entry(frame_form, width=30)
        entry_velocidad.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Caballaje:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_caballaje = tk.Entry(frame_form, width=30)
        entry_caballaje.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Plazas:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        entry_plazas = tk.Entry(frame_form, width=30)
        entry_plazas.grid(row=5, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="ACTUALIZAR", command=lambda: messagebox.showinfo("Éxito", "Auto actualizado"), width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_coches, width=15).pack(side="left", padx=10)
    
    def cambiar_camionetas(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ACTUALIZAR CAMIONETA", font=("Arial", 16)).pack(pady=20)
        
        frame_buscar = tk.Frame(self.root)
        frame_buscar.pack(pady=10)
        
        tk.Label(frame_buscar, text="ID de la camioneta a actualizar:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id_actualizar_camioneta = tk.Entry(frame_buscar, width=20)
        self.entry_id_actualizar_camioneta.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(frame_buscar, text="BUSCAR", command=self.buscar_camioneta_actualizar, width=10).grid(row=0, column=2, padx=10, pady=5)
        
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_camionetas, width=20).pack(pady=20)
        
    def buscar_camioneta_actualizar(self):
        id_camioneta = self.entry_id_actualizar_camioneta.get()
        if not id_camioneta:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        messagebox.showinfo("Buscar", f"Buscando camioneta ID: {id_camioneta}")

    def cambiar_camiones(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ACTUALIZAR CAMIÓN", font=("Arial", 16)).pack(pady=20)
        
        frame_buscar = tk.Frame(self.root)
        frame_buscar.pack(pady=10)
        
        tk.Label(frame_buscar, text="ID del camión a actualizar:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id_actualizar_camion = tk.Entry(frame_buscar, width=20)
        self.entry_id_actualizar_camion.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(frame_buscar, text="BUSCAR", command=self.buscar_camion_actualizar, width=10).grid(row=0, column=2, padx=10, pady=5)
        
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones_camiones, width=20).pack(pady=20)
        
    def buscar_camion_actualizar(self):
        id_camion = self.entry_id_actualizar_camion.get()
        if not id_camion:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        messagebox.showinfo("Buscar", f"Buscando camión ID: {id_camion}")

    def borrar_autos(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ELIMINAR AUTO", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="ID del auto a eliminar:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_eliminar_auto = tk.Entry(frame_form, width=30)
        self.entry_id_eliminar_auto.grid(row=0, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="ELIMINAR", command=self.eliminar_auto, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_coches, width=15).pack(side="left", padx=10)
        
    def eliminar_auto(self):
        id_auto = self.entry_id_eliminar_auto.get()
        if not id_auto:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el auto con ID: {id_auto}?")
        if confirmar:
            messagebox.showinfo("Éxito", f"Auto con ID: {id_auto} eliminado")

    def borrar_camionetas(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ELIMINAR CAMIONETA", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="ID de la camioneta a eliminar:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_eliminar_camioneta = tk.Entry(frame_form, width=30)
        self.entry_id_eliminar_camioneta.grid(row=0, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="ELIMINAR", command=self.eliminar_camioneta, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_camionetas, width=15).pack(side="left", padx=10)
        
    def eliminar_camioneta(self):
        id_camioneta = self.entry_id_eliminar_camioneta.get()
        if not id_camioneta:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la camioneta con ID: {id_camioneta}?")
        if confirmar:
            messagebox.showinfo("Éxito", f"Camioneta con ID: {id_camioneta} eliminada")

    def borrar_camiones(self):
        self.borrarPantalla()
        
        tk.Label(self.root, text="ELIMINAR CAMIÓN", font=("Arial", 16)).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="ID del camión a eliminar:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_eliminar_camion = tk.Entry(frame_form, width=30)
        self.entry_id_eliminar_camion.grid(row=0, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="ELIMINAR", command=self.eliminar_camion, width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=self.menu_acciones_camiones, width=15).pack(side="left", padx=10)
        
    def eliminar_camion(self):
        id_camion = self.entry_id_eliminar_camion.get()
        if not id_camion:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
            
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el camión con ID: {id_camion}?")
        if confirmar:
            messagebox.showinfo("Éxito", f"Camion con ID: {id_camion} eliminado")
        
    def ejecutar(self):
        self.menu_principal()
        self.root.mainloop()