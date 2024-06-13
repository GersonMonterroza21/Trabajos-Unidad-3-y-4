import tkinter as tk

root = tk.Tk()
root.geometry("1200x800")
root.title("Aplicación con Menú")
root.state('zoomed')

menu_frame = tk.Frame(root, bg='lightgrey', width=200, height=800)
menu_frame.pack(side='left', fill='y')

content_frame = tk.Frame(root, bg='white', width=1000, height=800)
content_frame.pack(side='right', fill='both', expand=True)

def cambiar_estado_boton(boton_activado):
    for boton in [btn_punto_funcion, btn_casos_usos, btn_punto_objeto, btn_acerca_de]:
        boton.config(bg='SystemButtonFace')
    boton_activado.config(bg='lightblue')

def limpiar_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def puntos_de_funcion():
    cambiar_estado_boton(btn_punto_funcion)
    limpiar_content_frame()
    contenido_label = tk.Label(content_frame, text="Contenido de Puntos de Función", font=('Helvetica', 24), bg='white')
    contenido_label.pack(pady=20)

def casos_de_uso():
    cambiar_estado_boton(btn_casos_usos)
    limpiar_content_frame()

    # Variables de control
    variables_valor = []
    totalTecnico = tk.DoubleVar(value=0)
    totalAmbiente = tk.DoubleVar(value=0)

    def crear_cuadro(titulo_tabla, x, y, simple, medio, complejo, ancho, largo):
        frame_cuadro = tk.Frame(content_frame, borderwidth=2, relief="groove", bg="#D6EAF8")
        frame_cuadro.place(relx=x, rely=y, relwidth=ancho, relheight=largo)

        nombre_tabla = []

        # Crear un Frame para el título y el botón
        title_button_frame = tk.Frame(frame_cuadro, bg="#D6EAF8")
        title_button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Crear y colocar el título del cuadro en el contenedor
        titulo_cuadro = tk.Label(title_button_frame, text=titulo_tabla, font=("Arial", 10), bg="#D6EAF8", fg="black")
        titulo_cuadro.pack(side="left")

        # Crear un botón "Agregar" dentro del contenedor
        button_agregar = tk.Button(title_button_frame, text="Agregar", command=lambda: agregar_item(table_frame, nombre_tabla, simple, medio, complejo))
        button_agregar.pack(side="right")

        # Crear un Frame para la "tabla" dentro del cuadro
        table_frame = tk.Frame(frame_cuadro, bg="#D6EAF8")
        table_frame.pack(pady=0, fill="both", expand=True)

        return table_frame, nombre_tabla

    def agregar_item(table_frame, nombre_tabla, simple, medio, complejo):
        popup = tk.Toplevel(root)
        popup.title("Agregar Entrada")

        tk.Label(popup, text="Nombre:", bg="#D6EAF8").grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg="#D6EAF8").grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set("Simple")
        tipo_menu = tk.OptionMenu(popup, tipo_var, "Simple", "Medio", "Complejo")
        tipo_menu.grid(row=1, column=1, pady=10)

        def guardar_item():
            nombre = nombre_entry.get()
            tipo = tipo_var.get()
            if nombre:
                valor = simple if tipo == "Simple" else (medio if tipo == "Medio" else complejo)
                nombre_tabla.append((nombre, tipo, valor))
                actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
                actualizar_total()

        tk.Button(popup, text="Guardar", command=guardar_item).grid(row=2, columnspan=2, pady=10)

    def editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        item = nombre_tabla[idx - 1]
        nombre_antiguo, tipo_antiguo, _ = item

        popup = tk.Toplevel(root)
        popup.title("Editar Entrada")

        tk.Label(popup, text="Nombre:", bg="#D6EAF8").grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.insert(0, nombre_antiguo)
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg="#D6EAF8").grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set(tipo_antiguo)
        tipo_menu = tk.OptionMenu(popup, tipo_var, "Simple", "Medio", "Complejo")
        tipo_menu.grid(row=1, column=1, pady=10)

        def guardar_edicion():
            nombre_nuevo = nombre_entry.get()
            tipo_nuevo = tipo_var.get()
            if nombre_nuevo:
                valor_nuevo = simple if tipo_nuevo == "Simple" else (medio if tipo_nuevo == "Medio" else complejo)
                nombre_tabla[idx - 1] = (nombre_nuevo, tipo_nuevo, valor_nuevo)
                actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
                actualizar_total()
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_edicion).grid(row=2, columnspan=2, pady=10)

    def eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        del nombre_tabla[idx - 1]
        actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
        actualizar_total()

    def actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo):
        for widget in table_frame.winfo_children():
            widget.destroy()

        tk.Label(table_frame, text="Nombre", bg="#5499C7").grid(row=0, column=0, sticky="nsew")
        tk.Label(table_frame, text="Tipo", bg="#5499C7").grid(row=0, column=1, sticky="nsew")
        tk.Label(table_frame, text="Valor", bg="#5499C7").grid(row=0, column=2, sticky="nsew")

        for i, (nombre, tipo, valor) in enumerate(nombre_tabla, start=1):
            tk.Label(table_frame, text=nombre).grid(row=i, column=0, sticky="nsew")
            tk.Label(table_frame, text=tipo).grid(row=i, column=1, sticky="nsew")
            tk.Label(table_frame, text=valor).grid(row=i, column=2, sticky="nsew")

            editar_button = tk.Button(table_frame, text="Editar", command=lambda idx=i: editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            editar_button.grid(row=i, column=3)

            eliminar_button = tk.Button(table_frame, text="Eliminar", command=lambda idx=i: eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            eliminar_button.grid(row=i, column=4)

    table_frame_entradas, itemsEntradas = crear_cuadro("Actores", 0.11, 0.73, 1, 2, 3, 0.22, 0.3)
    table_frame_salidas, itemsSalidas = crear_cuadro("Entradas", 0.11, 0.37, 1, 2, 3, 0.22, 0.3)
    table_frame_consultas, itemsConsultas = crear_cuadro("Consultas", 0.11, 0.01, 1, 2, 3, 0.22, 0.3)
    table_frame_internas, itemsInternas = crear_cuadro("Archivos Interesados", 0.11, 0.55, 1, 2, 3, 0.22, 0.3)
    table_frame_externas, itemsExternas = crear_cuadro("Archivos Interface", 0.11, 0.19, 1, 2, 3, 0.22, 0.3)

    def actualizar_total():
        total = sum(totalTecnico.get(), totalAmbiente.get())
        total_label.config(text=f"Total: {total}")

    total_label = tk.Label(content_frame, text="Total: 0", font=('Helvetica', 24), bg='white')
    total_label.pack(pady=20)

    # Calcular Puntos de Función
    calcular_button = tk.Button(content_frame, text="Calcular", command=actualizar_total)
    calcular_button.pack(pady=10)

    # Sección de contenido
    tk.Label(content_frame, text="Contenido de Casos de Uso", font=('Helvetica', 24), bg='white').pack(pady=20)

def puntos_de_objetos():
    cambiar_estado_boton(btn_punto_objeto)
    limpiar_content_frame()
    contenido_label = tk.Label(content_frame, text="Contenido de Puntos de Objetos", font=('Helvetica', 24), bg='white')
    contenido_label.pack(pady=20)

def acerca_de():
    cambiar_estado_boton(btn_acerca_de)
    limpiar_content_frame()
    contenido_label = tk.Label(content_frame, text="Contenido Acerca De", font=('Helvetica', 24), bg='white')
    contenido_label.pack(pady=20)

# Botones del menú
btn_punto_funcion = tk.Button(menu_frame, text="Puntos de Función", command=puntos_de_funcion, bg='SystemButtonFace', font=('Helvetica', 16), width=15)
btn_punto_funcion.pack(pady=10, padx=10, anchor='w')

btn_casos_usos = tk.Button(menu_frame, text="Casos de Uso", command=casos_de_uso, bg='SystemButtonFace', font=('Helvetica', 16), width=15)
btn_casos_usos.pack(pady=10, padx=10, anchor='w')

btn_punto_objeto = tk.Button(menu_frame, text="Puntos de Objetos", command=puntos_de_objetos, bg='SystemButtonFace', font=('Helvetica', 16), width=15)
btn_punto_objeto.pack(pady=10, padx=10, anchor='w')

btn_acerca_de = tk.Button(menu_frame, text="Acerca de", command=acerca_de, bg='SystemButtonFace', font=('Helvetica', 16), width=15)
btn_acerca_de.pack(pady=10, padx=10, anchor='w')

root.mainloop()
