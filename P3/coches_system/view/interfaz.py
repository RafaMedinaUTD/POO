import tkinter as tk
from tkinter import messagebox
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
    
    def crear_boton(self, texto, comando, width=20, height=2, bg=None, fg=None):
        btn = tk.Button(self.root, text=texto, command=comando, width=width, height=height)
        if bg:
            btn.config(bg=bg)
        if fg:
            btn.config(fg=fg)
        return btn
    
    def crear_titulo(self, texto, size=16):
        return tk.Label(self.root, text=texto, font=("Arial", size, "bold"))
    
    def menu_principal(self):
        self.borrarPantalla()
        
        self.crear_titulo("SISTEMA DE GESTIÓN DE COCHES", 16).pack(pady=20)
        self.crear_boton("AUTOS", self.menu_acciones_coches).pack(pady=10)
        self.crear_boton("CAMIONETAS", self.menu_acciones_camionetas).pack(pady=10)
        self.crear_boton("CAMIONES", self.menu_acciones_camiones).pack(pady=10)
        self.crear_boton("SALIR", self.root.quit).pack(pady=10)
    
    def crear_menu_acciones(self, titulo, insertar, consultar, actualizar, eliminar, regresar):
        self.borrarPantalla()
        self.crear_titulo(titulo, 14).pack(pady=20)
        self.crear_boton("INSERTAR", insertar).pack(pady=10)
        self.crear_boton("CONSULTAR", consultar).pack(pady=10)
        self.crear_boton("ACTUALIZAR", actualizar).pack(pady=10)
        self.crear_boton("ELIMINAR", eliminar).pack(pady=10)
        self.crear_boton("REGRESAR", regresar).pack(pady=10)
    
    def menu_acciones_coches(self):
        self.crear_menu_acciones("GESTIÓN DE AUTOS", self.insertar_autos, self.consultar_autos, 
                                self.cambiar_autos, self.borrar_autos, self.menu_principal)
    
    def menu_acciones_camionetas(self):
        self.crear_menu_acciones("GESTIÓN DE CAMIONETAS", self.insertar_camionetas, self.consultar_camionetas,
                                self.cambiar_camionetas, self.borrar_camionetas, self.menu_principal)
    
    def menu_acciones_camiones(self):
        self.crear_menu_acciones("GESTIÓN DE CAMIONES", self.insertar_camiones, self.consultar_camiones,
                                self.cambiar_camiones, self.borrar_camiones, self.menu_principal)
    
    def crear_formulario_entrada(self, titulo, campos, guardar_callback, cancelar_callback):
        self.borrarPantalla()
        self.crear_titulo(titulo).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        entries = {}
        for i, (label_text, tipo) in enumerate(campos.items()):
            tk.Label(frame_form, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            if tipo == "combobox":
                widget = ttk.Combobox(frame_form, width=28, state="readonly")
                widget['values'] = ('Si', 'No')
                widget.current(0)
            else:
                widget = tk.Entry(frame_form, width=30)
            
            widget.grid(row=i, column=1, padx=10, pady=5)
            entries[label_text.lower().replace(":", "").replace(" ", "_")] = widget
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="GUARDAR", command=lambda: guardar_callback(entries), width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=cancelar_callback, width=15).pack(side="left", padx=10)
        
        return entries
    
    def insertar_autos(self):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada"
        }
        self.crear_formulario_entrada("INSERTAR NUEVO AUTO", campos, self.guardar_auto, self.menu_acciones_coches)
    
    def guardar_auto(self, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        
        if not all([marca, color, modelo, velocidad, caballaje, plazas]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        resultado = self.controlador.insertar_auto(marca, color, modelo, velocidad, caballaje, plazas)
        self.controlador.respuesta_operacion("Insertar Auto", resultado)
        if resultado:
            self.mostrar_alerta("Auto agregado exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_coches)
        else:
            self.mostrar_alerta("Error al agregar el auto", tipo="error")
    
    def insertar_camionetas(self):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada",
            "Tracción:": "entrada",
            "Cerrada:": "combobox"
        }
        self.crear_formulario_entrada("INSERTAR NUEVA CAMIONETA", campos, self.guardar_camioneta, self.menu_acciones_camionetas)
    
    def guardar_camioneta(self, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        traccion = entries["tracción"].get()
        cerrada = entries["cerrada"].get()
        
        if not all([marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        resultado = self.controlador.insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        self.controlador.respuesta_operacion("Insertar Camioneta", resultado)
        if resultado:
            self.mostrar_alerta("Camioneta agregada exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_camionetas)
        else:
            self.mostrar_alerta("Error al agregar la camioneta", tipo="error")
    
    def insertar_camiones(self):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada",
            "Toneladas:": "entrada"
        }
        self.crear_formulario_entrada("INSERTAR NUEVO CAMIÓN", campos, self.guardar_camion, self.menu_acciones_camiones)
    
    def guardar_camion(self, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        toneladas = entries["toneladas"].get()
        
        if not all([marca, color, modelo, velocidad, caballaje, plazas, toneladas]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        resultado = self.controlador.insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, toneladas)
        self.controlador.respuesta_operacion("Insertar Camión", resultado)
        if resultado:
            self.mostrar_alerta("Camión agregado exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_camiones)
        else:
            self.mostrar_alerta("Error al agregar el camión", tipo="error")
    
    def mostrar_consulta_labels(self, titulo, datos_func, atributos, regresar_callback):
        self.borrarPantalla()
        self.crear_titulo(titulo).pack(pady=20)
        
        datos = datos_func()
        
        if not datos:
            tk.Label(self.root, text="No hay registros", font=("Arial", 12)).pack(pady=20)
        else:
            frame_contenedor = tk.Frame(self.root)
            frame_contenedor.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            canvas = tk.Canvas(frame_contenedor)
            scrollbar = tk.Scrollbar(frame_contenedor, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)
            
            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            for i, registro in enumerate(datos):
                frame_registro = tk.Frame(scrollable_frame, relief=tk.GROOVE, bd=2, padx=10, pady=10)
                frame_registro.pack(fill=tk.X, padx=5, pady=5)
                
                tk.Label(frame_registro, text=f"Registro #{i+1}", font=("Arial", 11, "bold")).pack(anchor="w")
                
                for j, valor in enumerate(registro):
                    etiqueta_texto = f"{atributos[j]}: {valor}"
                    tk.Label(frame_registro, text=etiqueta_texto, font=("Arial", 10), anchor="w", justify="left").pack(anchor="w", padx=10)
            
            canvas.pack(side="left", fill=tk.BOTH, expand=True)
            scrollbar.pack(side="right", fill=tk.Y)
        
        self.crear_boton("REGRESAR", regresar_callback, width=20).pack(pady=20)
    
    def consultar_autos(self):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        self.mostrar_consulta_labels("CONSULTAR AUTOS REGISTRADOS", 
                                    self.controlador.consultar_autos, 
                                    atributos, 
                                    self.menu_acciones_coches)
    
    def consultar_camionetas(self):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción", "Cerrada"]
        self.mostrar_consulta_labels("CONSULTAR CAMIONETAS REGISTRADAS", 
                                    self.controlador.consultar_camionetas, 
                                    atributos, 
                                    self.menu_acciones_camionetas)
    
    def consultar_camiones(self):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Toneladas"]
        self.mostrar_consulta_labels("CONSULTAR CAMIONES REGISTRADOS", 
                                    self.controlador.consultar_camiones, 
                                    atributos, 
                                    self.menu_acciones_camiones)
    
    def crear_formulario_actualizar(self, titulo, id_func, buscar_callback, regresar_callback):
        self.borrarPantalla()
        self.crear_titulo(titulo).pack(pady=20)
        
        frame_buscar = tk.Frame(self.root)
        frame_buscar.pack(pady=10)
        
        tk.Label(frame_buscar, text="ID a actualizar:").grid(row=0, column=0, padx=10, pady=5)
        entry_id = tk.Entry(frame_buscar, width=20)
        entry_id.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(frame_buscar, text="BUSCAR", command=lambda: buscar_callback(entry_id.get()), width=10).grid(row=0, column=2, padx=10, pady=5)
        
        self.crear_boton("REGRESAR", regresar_callback, width=20).pack(pady=20)
    
    def cambiar_autos(self):
        self.crear_formulario_actualizar("ACTUALIZAR AUTO", 
                                        self.controlador.consultar_auto_por_id,
                                        self.buscar_auto_actualizar,
                                        self.menu_acciones_coches)
    
    def buscar_auto_actualizar(self, id_auto):
        if not id_auto:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
        
        auto = self.controlador.consultar_auto_por_id(id_auto)
        if auto:
            self.mostrar_formulario_actualizar_auto(id_auto, auto)
        else:
            messagebox.showerror("Error", "Auto no encontrado")
    
    def mostrar_formulario_actualizar_auto(self, id_auto, auto):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada"
        }
        
        self.crear_formulario_actualizar_datos(f"ACTUALIZAR AUTO - ID: {id_auto}", 
                                             campos, auto, 
                                             lambda entries: self.ejecutar_actualizar_auto(id_auto, entries),
                                             self.menu_acciones_coches)
    
    def crear_formulario_actualizar_datos(self, titulo, campos, datos, guardar_callback, cancelar_callback):
        self.borrarPantalla()
        self.crear_titulo(titulo).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        entries = {}
        for i, (label_text, tipo) in enumerate(campos.items()):
            tk.Label(frame_form, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            if tipo == "combobox":
                widget = ttk.Combobox(frame_form, width=28, state="readonly")
                widget['values'] = ('Si', 'No')
                # Manejo especial para el campo "cerrada" que debe ser 'Si' o 'No'
                valor = str(datos[i+1]).strip()
                widget.set(valor if valor in ('Si', 'No') else 'Si')
            else:
                widget = tk.Entry(frame_form, width=30)
                widget.insert(0, datos[i+1])
            
            widget.grid(row=i, column=1, padx=10, pady=5)
            entries[label_text.lower().replace(":", "").replace(" ", "_")] = widget
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="ACTUALIZAR", command=lambda: guardar_callback(entries), width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=cancelar_callback, width=15).pack(side="left", padx=10)
        
        return entries
    
    def ejecutar_actualizar_auto(self, id_auto, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        
        resultado = self.controlador.actualizar_auto(id_auto, marca, color, modelo, velocidad, caballaje, plazas)
        self.controlador.respuesta_operacion("Actualizar Auto", resultado)
        if resultado:
            self.mostrar_alerta("Auto actualizado exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_coches)
        else:
            self.mostrar_alerta("Error al actualizar el auto", tipo="error")
    
    def cambiar_camionetas(self):
        self.crear_formulario_actualizar("ACTUALIZAR CAMIONETA",
                                        self.controlador.consultar_camioneta_por_id,
                                        self.buscar_camioneta_actualizar,
                                        self.menu_acciones_camionetas)
    
    def buscar_camioneta_actualizar(self, id_camioneta):
        if not id_camioneta:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
        
        camioneta = self.controlador.consultar_camioneta_por_id(id_camioneta)
        if camioneta:
            self.mostrar_formulario_actualizar_camioneta(id_camioneta, camioneta)
        else:
            messagebox.showerror("Error", "Camioneta no encontrada")
    
    def mostrar_formulario_actualizar_camioneta(self, id_camioneta, camioneta):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada",
            "Tracción:": "entrada",
            "Cerrada:": "combobox"
        }
        
        self.crear_formulario_actualizar_datos(f"ACTUALIZAR CAMIONETA - ID: {id_camioneta}",
                                             campos, camioneta,
                                             lambda entries: self.ejecutar_actualizar_camioneta(id_camioneta, entries),
                                             self.menu_acciones_camionetas)
    
    def ejecutar_actualizar_camioneta(self, id_camioneta, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        traccion = entries["tracción"].get()
        cerrada = entries["cerrada"].get()
        
        resultado = self.controlador.actualizar_camioneta(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
        self.controlador.respuesta_operacion("Actualizar Camioneta", resultado)
        if resultado:
            self.mostrar_alerta("Camioneta actualizada exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_camionetas)
        else:
            self.mostrar_alerta("Error al actualizar la camioneta", tipo="error")
    
    def cambiar_camiones(self):
        self.crear_formulario_actualizar("ACTUALIZAR CAMIÓN",
                                        self.controlador.consultar_camion_por_id,
                                        self.buscar_camion_actualizar,
                                        self.menu_acciones_camiones)
    
    def buscar_camion_actualizar(self, id_camion):
        if not id_camion:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
        
        camion = self.controlador.consultar_camion_por_id(id_camion)
        if camion:
            self.mostrar_formulario_actualizar_camion(id_camion, camion)
        else:
            messagebox.showerror("Error", "Camión no encontrado")
    
    def mostrar_formulario_actualizar_camion(self, id_camion, camion):
        campos = {
            "Marca:": "entrada",
            "Color:": "entrada",
            "Modelo:": "entrada",
            "Velocidad:": "entrada",
            "Caballaje:": "entrada",
            "Plazas:": "entrada",
            "Toneladas:": "entrada"
        }
        
        self.crear_formulario_actualizar_datos(f"ACTUALIZAR CAMIÓN - ID: {id_camion}",
                                             campos, camion,
                                             lambda entries: self.ejecutar_actualizar_camion(id_camion, entries),
                                             self.menu_acciones_camiones)
    
    def ejecutar_actualizar_camion(self, id_camion, entries):
        marca = entries["marca"].get()
        color = entries["color"].get()
        modelo = entries["modelo"].get()
        velocidad = entries["velocidad"].get()
        caballaje = entries["caballaje"].get()
        plazas = entries["plazas"].get()
        toneladas = entries["toneladas"].get()
        
        resultado = self.controlador.actualizar_camion(id_camion, marca, color, modelo, velocidad, caballaje, plazas, toneladas)
        self.controlador.respuesta_operacion("Actualizar Camión", resultado)
        if resultado:
            self.mostrar_alerta("Camión actualizado exitosamente", tipo="exito", regresar=True, menu_callback=self.menu_acciones_camiones)
        else:
            self.mostrar_alerta("Error al actualizar el camión", tipo="error")
    
    def crear_formulario_eliminar(self, titulo, consultar_func, eliminar_func, regresar_callback):
        self.borrarPantalla()
        self.crear_titulo(titulo).pack(pady=20)
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)
        
        tk.Label(frame_form, text="ID a eliminar:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_id = tk.Entry(frame_form, width=30)
        entry_id.grid(row=0, column=1, padx=10, pady=5)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="BUSCAR", command=lambda: self.buscar_eliminar(entry_id.get(), consultar_func, eliminar_func, regresar_callback), width=15).pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", command=regresar_callback, width=15).pack(side="left", padx=10)
    
    def buscar_eliminar(self, id_objeto, consultar_func, eliminar_func, regresar_callback):
        if not id_objeto:
            messagebox.showwarning("Advertencia", "Ingrese un ID")
            return
        
        objeto = consultar_func(id_objeto)
        if not objeto:
            messagebox.showerror("Error", "Registro no encontrado")
            return
        
        eliminar_func(id_objeto, objeto, regresar_callback)
    
    def mostrar_confirmacion_eliminar_con_scroll(self, titulo, atributos, datos, id_objeto, confirmar_callback, regresar_callback):
        self.borrarPantalla()
        
        self.crear_titulo(titulo, 16).pack(pady=20)
        
        frame_contenedor = tk.Frame(self.root)
        frame_contenedor.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(frame_contenedor)
        scrollbar = tk.Scrollbar(frame_contenedor, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        tk.Label(scrollable_frame, text=f"¿Está seguro de eliminar el siguiente registro?", font=("Arial", 12, "bold")).pack(pady=10)
        
        for i, valor in enumerate(datos):
            etiqueta_texto = f"{atributos[i]}: {valor}"
            tk.Label(scrollable_frame, text=etiqueta_texto, font=("Arial", 11), anchor="w", justify="left").pack(anchor="w", padx=20, pady=5)
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill=tk.Y)
        
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="CONFIRMAR ELIMINACIÓN", 
                 command=lambda: confirmar_callback(id_objeto, regresar_callback), 
                 width=25, height=2, bg="red", fg="white").pack(side="left", padx=10)
        tk.Button(frame_botones, text="CANCELAR", 
                 command=regresar_callback, 
                 width=25, height=2).pack(side="left", padx=10)
    
    def borrar_autos(self):
        self.crear_formulario_eliminar("ELIMINAR AUTO",
                                      self.controlador.consultar_auto_por_id,
                                      self.mostrar_confirmacion_eliminar_auto,
                                      self.menu_acciones_coches)
    
    def mostrar_confirmacion_eliminar_auto(self, id_auto, auto, regresar_callback):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        self.mostrar_confirmacion_eliminar_con_scroll(
            "CONFIRMAR ELIMINACIÓN DE AUTO",
            atributos,
            auto,
            id_auto,
            self.confirmar_eliminar_auto,
            regresar_callback
        )
    
    def confirmar_eliminar_auto(self, id_auto, regresar_callback):
        resultado = self.controlador.eliminar_auto(id_auto)
        self.controlador.respuesta_operacion("Eliminar Auto", resultado)
        if resultado:
            self.mostrar_alerta("Auto eliminado exitosamente", tipo="exito", regresar=True, menu_callback=regresar_callback)
        else:
            self.mostrar_alerta("Error al eliminar el auto", tipo="error", regresar=True, menu_callback=regresar_callback)
    
    def borrar_camionetas(self):
        self.crear_formulario_eliminar("ELIMINAR CAMIONETA",
                                      self.controlador.consultar_camioneta_por_id,
                                      self.mostrar_confirmacion_eliminar_camioneta,
                                      self.menu_acciones_camionetas)
    
    def mostrar_confirmacion_eliminar_camioneta(self, id_camioneta, camioneta, regresar_callback):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción", "Cerrada"]
        self.mostrar_confirmacion_eliminar_con_scroll(
            "CONFIRMAR ELIMINACIÓN DE CAMIONETA",
            atributos,
            camioneta,
            id_camioneta,
            self.confirmar_eliminar_camioneta,
            regresar_callback
        )
    
    def confirmar_eliminar_camioneta(self, id_camioneta, regresar_callback):
        resultado = self.controlador.eliminar_camioneta(id_camioneta)
        self.controlador.respuesta_operacion("Eliminar Camioneta", resultado)
        if resultado:
            self.mostrar_alerta("Camioneta eliminada exitosamente", tipo="exito", regresar=True, menu_callback=regresar_callback)
        else:
            self.mostrar_alerta("Error al eliminar la camioneta", tipo="error", regresar=True, menu_callback=regresar_callback)
    
    def borrar_camiones(self):
        self.crear_formulario_eliminar("ELIMINAR CAMIÓN",
                                      self.controlador.consultar_camion_por_id,
                                      self.mostrar_confirmacion_eliminar_camion,
                                      self.menu_acciones_camiones)
    
    def mostrar_confirmacion_eliminar_camion(self, id_camion, camion, regresar_callback):
        atributos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Toneladas"]
        self.mostrar_confirmacion_eliminar_con_scroll(
            "CONFIRMAR ELIMINACIÓN DE CAMIÓN",
            atributos,
            camion,
            id_camion,
            self.confirmar_eliminar_camion,
            regresar_callback
        )
    
    def confirmar_eliminar_camion(self, id_camion, regresar_callback):
        resultado = self.controlador.eliminar_camion(id_camion)
        self.controlador.respuesta_operacion("Eliminar Camión", resultado)
        if resultado:
            self.mostrar_alerta("Camión eliminado exitosamente", tipo="exito", regresar=True, menu_callback=regresar_callback)
        else:
            self.mostrar_alerta("Error al eliminar el camión", tipo="error", regresar=True, menu_callback=regresar_callback)
    
    def mostrar_alerta(self, mensaje, tipo="info", regresar=False, menu_callback=None):
        if tipo == "exito":
            messagebox.showinfo("Éxito", mensaje)
        elif tipo == "error":
            messagebox.showerror("Error", mensaje)
        else:
            messagebox.showinfo("Información", mensaje)
        
        if regresar and callable(menu_callback):
            menu_callback()
    
    def ejecutar(self):
        self.menu_principal()
        self.root.mainloop()