import tkinter as tk

class InterfazAutos:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Sistema de Coches")
        self.root.geometry("600x400")
        
    def menu_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="SISTEMA DE GESTIÓN DE COCHES", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="AUTOS", command=self.menu_acciones, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="SALIR", command=self.root.quit, width=20, height=2).pack(pady=10)
        
    def menu_acciones(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="GESTIÓN DE AUTOS", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="INSERTAR", command=self.insertar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="CONSULTAR", command=self.consultar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ACTUALIZAR", command=self.cambiar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="ELIMINAR", command=self.borrar_autos, width=20, height=2).pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_principal, width=20, height=2).pack(pady=10)
        
    def insertar_autos(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="INSERTAR AUTO", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Formulario para insertar auto").pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones, width=20).pack(pady=20)
        
    def consultar_autos(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="CONSULTAR AUTOS", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Lista de autos registrados").pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones, width=20).pack(pady=20)
        
    def cambiar_autos(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="ACTUALIZAR AUTO", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Formulario para actualizar auto").pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones, width=20).pack(pady=20)
        
    def borrar_autos(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="ELIMINAR AUTO", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Formulario para eliminar auto").pack(pady=10)
        tk.Button(self.root, text="REGRESAR", command=self.menu_acciones, width=20).pack(pady=20)
        
    def ejecutar(self):
        self.menu_principal()
        self.root.mainloop()