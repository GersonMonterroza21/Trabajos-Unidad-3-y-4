import tkinter as tk
from tkinter import ttk

# Crear la root principal
root = tk.Tk()
root.geometry("1200x800")  # Establecer las dimensiones de la root
root.title("Aplicación con Menú")
root.state('zoomed')

# Crear un Frame para el menú lateral
menu_frame = tk.Frame(root, bg='lightgrey', width=200, height=800)
menu_frame.pack(side='left', fill='y')

# Crear un Frame para el contenido principal
content_frame = tk.Frame(root, bg='white', width=1000, height=800)
content_frame.pack(side='right', fill='both', expand=True)
#Funcion que controla la actividad de los botones
def cambiar_estado_boton(boton_activado):
    for boton in [btn_punto_funcion, btn_casos_usos, btn_punto_objeto, btn_acerca_de]:
        boton.config(bg='SystemButtonFace')

    boton_activado.config(bg='lightblue')

# Funciones para los botones del menú
def puntos_de_funcion():
    cambiar_estado_boton(btn_punto_funcion)
    # Colores globales
    cuadro = tk.Canvas(root, width=root.winfo_screenwidth() * 0.92, height=root.winfo_screenheight() * 1.0, bg="white")
    pos_x = root.winfo_screenwidth() * 0.08  # Posición x al 10% del ancho de la pantalla
    pos_y = root.winfo_screenheight() * 0.0  # Posición y al 10% del alto de la pantalla
    cuadro.place(x=pos_x, y=pos_y)


    COLOR_FONDO = "#D6EAF8"         # Light Blue
    COLOR_TITULO = "#000000"        # Dark Blue
    COLOR_BORDE = "groove"          # Groove
    COLOR_BORDE_INTERNO = "solid"   # Solid
    COLOR_ETIQUETA = "#5499C7"      # Sky Blue

    # contador
    contador = 0
    contadorFilas = 0

    # Variable de control
    variables_valor = []

    def crear_cuadro(titulo_tabla, x, y, simple, medio, complejo):
        frame_cuadro = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_cuadro.place(relx=x, rely=y, relwidth=0.25, relheight=0.3)

        # Lista para almacenar los ítems (nombre, tipo, valor)
        nombre_tabla = []

        # Crear un Frame para el título y el botón
        title_button_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        title_button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Crear y colocar el título del cuadro en el contenedor
        titulo_cuadro = tk.Label(title_button_frame, text=titulo_tabla, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_cuadro.pack(side="left")

        # Crear un botón "Agregar" dentro del contenedor
        button_agregar = tk.Button(title_button_frame, text="Agregar", command=lambda: agregar_item(table_frame, nombre_tabla, simple, medio, complejo))
        button_agregar.pack(side="right")

        # Crear un Frame para la "tabla" dentro del cuadro
        table_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        table_frame.pack(pady=0, fill="both", expand=True)

        return table_frame, nombre_tabla

    # ------------------------------------------------------------------------------------------

    def agregar_item(table_frame, nombre_tabla, simple, medio, complejo):
        popup = tk.Toplevel(root)
        popup.title("Agregar Entrada")

        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set("Simple")  # Valor predeterminado
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
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_item).grid(row=2, columnspan=2, pady=10)

    def editar_item(table_frame, idx, nombre_tabla, medio, simple, complejo):
        item = nombre_tabla[idx - 1]  # Obtenemos el elemento correspondiente al índice
        nombre_antiguo, tipo_antiguo, _ = item  # Desempaquetamos el elemento

        # Crear la root emergente para la edición
        popup = tk.Toplevel(root)
        popup.title("Editar Entrada")

        # Campos prellenados con los valores antiguos
        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.insert(0, nombre_antiguo)  # Poner el valor antiguo en el campo
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set(tipo_antiguo)  # Poner el valor antiguo como seleccionado
        tipo_menu = tk.OptionMenu(popup, tipo_var, "Simple", "Medio", "Complejo")
        tipo_menu.grid(row=1, column=1, pady=10)

        def guardar_edicion():
            nombre_nuevo = nombre_entry.get()
            tipo_nuevo = tipo_var.get()
            if nombre_nuevo:
                valor_nuevo = simple if tipo_nuevo == "Simple" else (medio if tipo_nuevo == "Medio" else complejo)
                nombre_tabla[idx - 1] = (nombre_nuevo, tipo_nuevo, valor_nuevo) # Actualizar la lista con los nuevos valores
                actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
                actualizar_total()
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_edicion).grid(row=2, columnspan=2, pady=10)

    def eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        del nombre_tabla[idx - 1]  # Restamos 1 porque el índice del widget comienza en 1, pero en la lista comienza en 0
        actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
        actualizar_total()

    def actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo):
        # Limpiar la tabla
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Títulos de la tabla
        tk.Label(table_frame, text="Nombre", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=0, column=0, sticky="nsew")
        tk.Label(table_frame, text="Tipo", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=1, sticky="nsew")
        tk.Label(table_frame, text="Valor", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=2, sticky="nsew")

        # Agregar datos a la tabla
        contador = 0
        contadorFilas = 0
        for i, (nombre, tipo, valor) in enumerate(nombre_tabla, start=1):
            tk.Label(table_frame, text=nombre, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10).grid(row=i, column=0, sticky="nsew")
            tk.Label(table_frame, text=tipo, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8).grid(row=i, column=1, sticky="nsew")
            tk.Label(table_frame, text=valor, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8).grid(row=i, column=2, sticky="nsew")
            # Botones para editar y eliminar el ítem
            editar_button = tk.Button(table_frame, text="Editar", command=lambda idx=i: editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            editar_button.grid(row=i, column=3)
            eliminar_button = tk.Button(table_frame, text="Eliminar", command=lambda idx=i: eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            eliminar_button.grid(row=i, column=4)

            contador += valor
            contadorFilas = i

        # Fila del total
        tk.Label(table_frame, text="TOTAL", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=0, sticky="nsew")
        tk.Label(table_frame, text="", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=1, sticky="nsew")
        tk.Label(table_frame, text=contador, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=2, sticky="nsew")


    # ----------------------------------------------------------------------------------------
    # Crear un Frame para la sección que ocupe el 40% del tamaño de la root

    def crear_seccion(x, y):
        # Arreglo de los factores
        factores_puntos_funcion = [
            "Entradas Externas (EE)",
            "Salidas Externas (SE)",
            "Consultas Externas (CE)",
            "Archivos Lógicos Internos (ALI)",
            "Archivos de Interfaz Externos (AIE)",
            "Datos Compartidos entre Aplicaciones (SCI)",
            "Interfaces Externas (EIF)",
            "Transacciones en Línea (TEL)",
            "Funciones Complejas (FC)",
            "Procesamiento Distribuido (DI)",
            "Reusabilidad (RE)",
            "Facilidad de Instalación (IE)",
            "Facilidad de Operación (OE)",
            "Facilidad de Cambio (CE)"
        ]

        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=x, rely=y, relwidth=0.4, relheight=0.75)

        # Crear un Frame para la tabla dentro de la sección
        table_frame = tk.Frame(frame_seccion, bg=COLOR_FONDO)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Título de la tabla
        tk.Label(table_frame, text="Factor de Ajuste de Valor (FAV)", font=("Arial", 12, "bold"), bg=COLOR_FONDO).grid(row=0, column=0, columnspan=3, pady=(0, 10), sticky="nsew")

        # Títulos de las columnas
        tk.Label(table_frame, text="N°", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=5, bg=COLOR_ETIQUETA).grid(row=1, column=0, sticky="nsew")
        tk.Label(table_frame, text="Factor", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=40, bg=COLOR_ETIQUETA).grid(row=1, column=1, sticky="nsew")
        tk.Label(table_frame, text="Valor", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=1, column=2, sticky="nsew")

        # Lista para almacenar las variables de control
        #variables_valor = []

        # Agregar datos a la tabla
        for i in range(1, 15):
            # Crear y posicionar las etiquetas y menús desplegables
            tk.Label(table_frame, text=i, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=5, bg=COLOR_ETIQUETA).grid(row=i + 1, column=0, sticky="nsew")
            tk.Label(table_frame, text=factores_puntos_funcion[i-1], borderwidth=1, relief=COLOR_BORDE_INTERNO, width=40, bg=COLOR_ETIQUETA).grid(row=i + 1, column=1, sticky="nsew")
            valor_var = tk.IntVar(value=0)  # Valor inicial en 0
            valor_menu = tk.OptionMenu(table_frame, valor_var, *range(6))  # Menú desplegable de 0 a 5
            valor_menu.grid(row=i + 1, column=2, sticky="nsew")
            variables_valor.append(valor_var)  # Almacenar la variable de control en la lista
            valor_var.trace_add("write", lambda name, index, mode, var=valor_var: actualizar_suma(variables_valor, total_label, resultado_label))

        # Total de la suma de los factores
        tk.Label(table_frame, text="TOTAL", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=5, bg=COLOR_ETIQUETA).grid(row=16, column=0, columnspan=2, sticky="nsew")
        total_label = tk.Label(table_frame, text="0", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA)
        total_label.grid(row=16, column=2, sticky="nsew")

        # Resultado final debajo de la tabla
        resultado_label = tk.Label(frame_seccion, text="Total de Puntos de Función: 0", font=("Arial", 10, "bold"), bg=COLOR_FONDO)
        resultado_label.pack(pady=(10, 0))

        actualizar_suma(variables_valor, total_label, resultado_label)
    # ------------------------------------------------------------------------------------------
    def crear_seccion_resultado(titulo):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=0.36, rely=0.61, relwidth=0.25, relheight=0.15)

        # Título de la sección
        titulo_label = tk.Label(frame_seccion, text=titulo, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_label.pack(pady=10)

        # Etiqueta para el valor del resultado
        valor_resultante = tk.Label(frame_seccion, text="0", font=("Arial", 12), bg=COLOR_FONDO)
        valor_resultante.pack(pady=10)

        return frame_seccion, valor_resultante

    #---------------------------------------------------------------------------------------------


    def crear_seccion_calculo(titulo):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=0.36, rely=0.76, relwidth=0.25, relheight=0.15)

        # Título de la sección
        titulo_label = tk.Label(frame_seccion, text=titulo, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_label.pack(pady=10)

        # Etiqueta para el valor del resultado
        valor_resultado = tk.Label(frame_seccion, text="0", font=("Arial", 12), bg=COLOR_FONDO)
        valor_resultado.pack(pady=10)

        return frame_seccion, valor_resultado
    # -------------------------------------------------------------------------------------

    #Control de los totales

    def actualizar_total():
        total = 0
        for items in [itemsEntradas, itemsSalidas, itemsPeticiones, itemsArchivos, itemsInterfaces]:
            total += sum(valor for _, _, valor in items)
        resultado_label.config(text=str(total))

    def actualizar_suma(variables_valor, total_label, resultado_label):
        suma_valores = sum(variable.get() for variable in variables_valor)
        total_label.config(text=str(suma_valores))
        resultado_label.config(text=f"Total de Puntos de Función: {suma_valores}")

    def actualizar_total_final():
        total = 0
        for items in [itemsEntradas, itemsSalidas, itemsPeticiones, itemsArchivos, itemsInterfaces]:
            total += sum(valor for _, _, valor in items)
        suma_valores = sum(variable.get() for variable in variables_valor)
        puntos_ajustados = round(total * (0.65 + (0.01 * suma_valores)), 2)
        valor_resultado.config(text=str(puntos_ajustados))

        root.after(100, actualizar_total_final)

    #----------------------------------------------------------------

    table_frame_entradas, itemsEntradas = crear_cuadro("Número de entradas de Usuario", 0.11, 0.01, 3, 4, 6)
    table_frame_salidas, itemsSalidas = crear_cuadro("Número de salidas de Usuario", 0.11, 0.31, 4, 5, 7)
    table_frame_peticioines, itemsPeticiones = crear_cuadro("Número de peticiones de Usuario", 0.11, 0.61, 3, 4, 6)
    table_frame_archivos, itemsArchivos = crear_cuadro("Número de Archivos", 0.36, 0.01, 7, 10, 15)
    table_frame_interfaces, itemsInterfaces = crear_cuadro("Número de Interfaces externas", 0.36, 0.31, 5, 7, 10)

    crear_seccion(0.61, 0.01)

    _, resultado_label = crear_seccion_resultado("Conteo Total")


    # Crear la sección de cálculo una vez
    _, valor_resultado = crear_seccion_calculo("Puntos de Función Ajustados")


    # Mostrar la tabla inicialmente
    actualizar_tabla(table_frame_entradas, itemsEntradas)
    actualizar_tabla(table_frame_salidas, itemsSalidas)
    actualizar_tabla(table_frame_peticioines, itemsPeticiones)
    actualizar_tabla(table_frame_archivos, itemsArchivos)
    actualizar_tabla(table_frame_interfaces, itemsInterfaces)

    actualizar_total()
    actualizar_total_final()


def casos_de_uso():
    cambiar_estado_boton(btn_casos_usos)

    cuadro = tk.Canvas(root, width=root.winfo_screenwidth() * 0.92, height=root.winfo_screenheight() * 1.0, bg="white")
    pos_x = root.winfo_screenwidth() * 0.08  # Posición x al 10% del ancho de la pantalla
    pos_y = root.winfo_screenheight() * 0.0  # Posición y al 10% del alto de la pantalla
    cuadro.place(x=pos_x, y=pos_y)

    COLOR_FONDO = "#D6EAF8"         # Light Blue
    COLOR_TITULO = "#000000"        # Dark Blue
    COLOR_BORDE = "groove"          # Groove
    COLOR_BORDE_INTERNO = "solid"   # Solid
    COLOR_ETIQUETA = "#5499C7"      # Sky Blue

    # contadores
    contador = 0
    contadorFilas = 0

    # Variables de control
    variables_valor = []
    totalTecnico = 0
    totalAmbiente = 0

    def crear_cuadro(titulo_tabla, x, y, simple, medio, complejo, ancho, largo):
        frame_cuadro = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_cuadro.place(relx=x, rely=y, relwidth=ancho, relheight=largo)

        # Lista para almacenar los ítems (nombre, tipo, valor)
        nombre_tabla = []

        # Crear un Frame para el título y el botón
        title_button_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        title_button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Crear y colocar el título del cuadro en el contenedor
        titulo_cuadro = tk.Label(title_button_frame, text=titulo_tabla, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_cuadro.pack(side="left")

        # Crear un botón "Agregar" dentro del contenedor
        button_agregar = tk.Button(title_button_frame, text="Agregar", command=lambda: agregar_item(table_frame, nombre_tabla, simple, medio, complejo))
        button_agregar.pack(side="right")

        # Crear un Frame para la "tabla" dentro del cuadro
        table_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        table_frame.pack(pady=0, fill="both", expand=True)

        return table_frame, nombre_tabla

    # ------------------------------------------------------------------------------------------

    def agregar_item(table_frame, nombre_tabla, simple, medio, complejo):
        popup = tk.Toplevel(root)
        popup.title("Agregar Entrada")

        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set("Simple")  # Valor predeterminado
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
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_item).grid(row=2, columnspan=2, pady=10)

    def editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        item = nombre_tabla[idx - 1]  # Obtenemos el elemento correspondiente al índice
        nombre_antiguo, tipo_antiguo, _ = item  # Desempaquetamos el elemento

        # Crear la root emergente para la edición
        popup = tk.Toplevel(root)
        popup.title("Editar Entrada")

        # Campos prellenados con los valores antiguos
        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.insert(0, nombre_antiguo)  # Poner el valor antiguo en el campo
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set(tipo_antiguo)  # Poner el valor antiguo como seleccionado
        tipo_menu = tk.OptionMenu(popup, tipo_var, "Simple", "Medio", "Complejo")
        tipo_menu.grid(row=1, column=1, pady=10)

        def guardar_edicion():
            nombre_nuevo = nombre_entry.get()
            tipo_nuevo = tipo_var.get()
            if nombre_nuevo:
                valor_nuevo = simple if tipo_nuevo == "Simple" else (medio if tipo_nuevo == "Medio" else complejo)
                nombre_tabla[idx - 1] = (nombre_nuevo, tipo_nuevo, valor_nuevo) # Actualizar la lista con los nuevos valores
                actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
                actualizar_total()
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_edicion).grid(row=2, columnspan=2, pady=10)

    def eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        del nombre_tabla[idx - 1]  # Restamos 1 porque el índice del widget comienza en 1, pero en la lista comienza en 0
        actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
        actualizar_total()

    def actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo):
        # Limpiar la tabla
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Títulos de la tabla
        tk.Label(table_frame, text="Nombre", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=0, column=0, sticky="nsew")
        tk.Label(table_frame, text="Tipo", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=1, sticky="nsew")
        tk.Label(table_frame, text="Valor", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=4, bg=COLOR_ETIQUETA).grid(row=0, column=2, sticky="nsew")

        # Agregar datos a la tabla
        contador = 0
        contadorFilas = 0
        for i, (nombre, tipo, valor) in enumerate(nombre_tabla, start=1):
            tk.Label(table_frame, text=nombre, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10).grid(row=i, column=0, sticky="nsew")
            tk.Label(table_frame, text=tipo, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8).grid(row=i, column=1, sticky="nsew")
            tk.Label(table_frame, text=valor, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=4).grid(row=i, column=2, sticky="nsew")
            # Botones para editar y eliminar el ítem
            editar_button = tk.Button(table_frame, text="Editar", command=lambda idx=i: editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            editar_button.grid(row=i, column=3)
            eliminar_button = tk.Button(table_frame, text="Eliminar", command=lambda idx=i: eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            eliminar_button.grid(row=i, column=4)

            contador += valor
            contadorFilas = i

        # Fila del total
        tk.Label(table_frame, text="TOTAL", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=0, sticky="nsew")
        tk.Label(table_frame, text="", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=1, sticky="nsew")
        tk.Label(table_frame, text=contador, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=4, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=2, sticky="nsew")


    # ----------------------------------------------------------------------------------------
    # Crear un Frame para la sección que ocupe el 40% del tamaño de la root

    def actualizar_suma(variables_valor, total_labels, total_label, resultado_label, factores, nombre_total):
        global totalTecnico
        global totalAmbiente
        total_general_Uno = 0
        total_general_Dos = 0
        for i, var in enumerate(variables_valor):
            peso = list(factores.values())[i]
            total = var.get() * peso
            total_labels[i].config(text=str(total))
            total_general_Uno += total
        if nombre_total == "Factor Técnico":
            total_general_Dos = round(0.6+(0.01*total_general_Uno),2)
            totalTecnico = total_general_Dos
        else:
            total_general_Dos = round(1.4 - (0.03*total_general_Uno),2)
            totalAmbiente = total_general_Dos
        total_label.config(text=str(total_general_Uno))
        resultado_label.config(text=f"{nombre_total}: {total_general_Dos}")
    
    #Arreglo de los factores Técnicos
    factores_tecnicos = {
            "Sistema Distribuido": 2,
            "Objetivos de performance o tiempo de respuesta": 1,
            "Eficiencia del usuario final": 1,
            "Procesamiento interno complejo": 1,
            "El código debe ser reutilizable": 1,
            "Facilidad de instalación": 0.5,
            "Facilidad de uso": 0.5,
            "Portabilidad": 2,
            "Facilidad de cambio": 1,
            "Concurrencia": 1,
            "Objetivos especiales de seguridad": 1,
            "Acceso directo a terceras partes": 1,
            "Facilidades especiales de entrenamiento a usuarios": 1
        }
    #Arreglo de los factores Ambientales
    factores_ambientales = {
        "Familiaridad con el modelo del proyecto utilizado": 1.5,
        "Experiencia en la aplicación": 0.5,
        "Experiencia en orientación a objetos": 1,
        "Capacidad del analista líder": 0.5,
        "Motivación": 1,
        "Estabilidad de los requerimientos": 2,
        "Personal a tiempo parcial": -1,
        "Dificultad del lenguaje de programación": -1
        }


    def crear_seccion(x, y, factores, ancho, largo, nombre_total):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=x, rely=y, relwidth=ancho, relheight=largo)

        # Crear un Frame para la tabla dentro de la sección
        table_frame = tk.Frame(frame_seccion, bg=COLOR_FONDO)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Título de la tabla
        tk.Label(table_frame, text="Factores Técnicos", font=("Arial", 12, "bold"), bg=COLOR_FONDO).grid(row=0, column=0, columnspan=5, pady=(0, 10), sticky="nsew")

        tk.Label(table_frame, text="Factor", borderwidth=1, font=("Arial", 8, "bold"), relief=COLOR_BORDE_INTERNO, width=5, bg=COLOR_ETIQUETA).grid(row=0, column=0, sticky="nsew")
        tk.Label(table_frame, text="Descripción", borderwidth=1, font=("Arial", 8, "bold"), relief=COLOR_BORDE_INTERNO, width=40, bg=COLOR_ETIQUETA).grid(row=0, column=1, sticky="nsew")
        tk.Label(table_frame, text="Peso", borderwidth=1, font=("Arial", 8, "bold"), relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=2, sticky="nsew")
        tk.Label(table_frame, text="Estimación", borderwidth=1, font=("Arial", 8, "bold"), relief=COLOR_BORDE_INTERNO, width=7, bg=COLOR_ETIQUETA).grid(row=0, column=3, sticky="nsew")
        tk.Label(table_frame, text="Total", borderwidth=1, font=("Arial", 8, "bold"), relief=COLOR_BORDE_INTERNO, width=7, bg=COLOR_ETIQUETA).grid(row=0, column=4, sticky="nsew")

        # Lista para almacenar las variables de control y las etiquetas de total
        variables_valor = []
        total_labels = []

        # Agregar datos a la tabla
        conteo = 0  # Comienza desde 0
        for factor, peso in factores.items():
            # Crear y posicionar las etiquetas y menús desplegables
            tk.Label(table_frame, text=f"T{conteo + 1}", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=5, bg=COLOR_ETIQUETA).grid(row=conteo + 1, column=0, sticky="nsew")
            tk.Label(table_frame, text=factor, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=40, bg=COLOR_ETIQUETA).grid(row=conteo + 1, column=1, sticky="nsew")
            tk.Label(table_frame, text=peso, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=conteo + 1, column=2, sticky="nsew")
            valor_var = tk.IntVar(value=0)  # Valor inicial en 0
            valor_menu = tk.OptionMenu(table_frame, valor_var, *range(6))  # Menú desplegable de 0 a 5
            valor_menu.grid(row=conteo + 1, column=3, sticky="nsew")
            variables_valor.append(valor_var)  # Almacenar la variable de control en la lista

            # Crear y almacenar la etiqueta para la columna "Total"
            total_label = tk.Label(table_frame, text="0", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=7, bg=COLOR_ETIQUETA)
            total_label.grid(row=conteo + 1, column=4, sticky="nsew")
            total_labels.append(total_label)

            # Vincular la actualización de la suma a cambios en el menú desplegable
            valor_var.trace_add("write", lambda name, index, mode, var=valor_var, peso=peso, i=conteo: actualizar_suma(variables_valor, total_labels, total_label_general, resultado_label, factores, nombre_total))

            conteo += 1

        # Total de la suma de los factores
        tk.Label(table_frame, text="TOTAL", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=65, bg=COLOR_ETIQUETA).grid(row=conteo + 1, column=0, columnspan=4, sticky="nsew")
        total_label_general = tk.Label(table_frame, text="0", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA)
        total_label_general.grid(row=conteo + 1, column=4, sticky="nsew")

        # Resultado final debajo de la tabla
        resultado_label = tk.Label(frame_seccion, text=f"{nombre_total}: 0", font=("Arial", 10, "bold"), bg=COLOR_FONDO)
        resultado_label.pack(pady=(10, 0))

        actualizar_suma(variables_valor, total_labels, total_label_general, resultado_label, factores, nombre_total)


    # ------------------------------------------------------------------------------------------
    def crear_seccion_resultado(titulo, x, y, ancho, largo):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=x, rely=y, relwidth=ancho, relheight=largo)

        # Título de la sección
        titulo_label = tk.Label(frame_seccion, text=titulo, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_label.pack(pady=10)

        # Etiqueta para el valor del resultado
        valor_resultante = tk.Label(frame_seccion, text="0", font=("Arial", 12), bg=COLOR_FONDO)
        valor_resultante.pack(pady=10)

        return frame_seccion, valor_resultante

    #---------------------------------------------------------------------------------------------


    def crear_seccion_calculo(titulo, x, y, ancho, largo):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=x, rely=y, relwidth=ancho, relheight=largo)

        # Título de la sección
        titulo_label = tk.Label(frame_seccion, text=titulo, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_label.pack(pady=10)

        # Etiqueta para el valor del resultado
        valor_resultado = tk.Label(frame_seccion, text="0", font=("Arial", 12), bg=COLOR_FONDO)
        valor_resultado.pack(pady=10)

        return frame_seccion, valor_resultado
    # -------------------------------------------------------------------------------------

    #Control de los totales

    def actualizar_total():
        total = 0
        for items in [itemsEntradas, itemsSalidas]:
            total += sum(valor for _, _, valor in items)
        resultado_label.config(text=str(total))

    

    def actualizar_total_final():
        global totalTecnico
        global totalAmbiente
        puntosSinAjustar = 0
        for items in [itemsEntradas, itemsSalidas]:
            puntosSinAjustar += sum(valor for _, _, valor in items)
        puntos_ajustados = round(puntosSinAjustar*totalTecnico*totalAmbiente, 2)
        valor_resultado.config(text=str(puntos_ajustados))

        root.after(100, actualizar_total_final)

    #----------------------------------------------------------------

    table_frame_entradas, itemsEntradas = crear_cuadro("Actores", 0.11, 0.73, 1, 2, 3, 0.22, 0.3)
    table_frame_salidas, itemsSalidas = crear_cuadro("Casos de Usos", 0.33, 0.73, 5, 10, 15, 0.22, 0.3)
   

    crear_seccion(0.11, 0.01, factores_tecnicos, 0.45, 0.72, "Factor Técnico")
    crear_seccion(0.56, 0.01, factores_ambientales, 0.45, 0.5, "Factor Ambiental")

    _, resultado_label = crear_seccion_resultado("Puntos de Casos de Uso sin Ajustar", 0.66, 0.51, 0.25, 0.15)


    # Crear la sección de cálculo una vez
    _, valor_resultado = crear_seccion_calculo("Puntos de Casos de Usos Ajustados", 0.71, 0.80, 0.25, 0.15)


    # Mostrar la tabla inicialmente
    actualizar_tabla(table_frame_entradas, itemsEntradas, 1, 2, 3)
    actualizar_tabla(table_frame_salidas, itemsSalidas, 5, 10, 15)

    actualizar_total()
    actualizar_total_final()



def puntos_objeto():
    cambiar_estado_boton(btn_punto_objeto)

    cuadro = tk.Canvas(root, width=root.winfo_screenwidth() * 0.92, height=root.winfo_screenheight() * 1.0, bg="white")
    pos_x = root.winfo_screenwidth() * 0.08  # Posición x al 10% del ancho de la pantalla
    pos_y = root.winfo_screenheight() * 0.0  # Posición y al 10% del alto de la pantalla
    cuadro.place(x=pos_x, y=pos_y)

    COLOR_FONDO = "#D6EAF8"         # Light Blue
    COLOR_TITULO = "#000000"        # Dark Blue
    COLOR_BORDE = "groove"          # Groove
    COLOR_BORDE_INTERNO = "solid"   # Solid
    COLOR_ETIQUETA = "#5499C7"      # Sky Blue

    # contador
    contador = 0
    contadorFilas = 0

    # Variable de control
    variables_valor = []

    def crear_cuadro(titulo_tabla, x, y, simple, medio, complejo):
        frame_cuadro = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_cuadro.place(relx=x, rely=y, relwidth=0.25, relheight=0.3)

        # Lista para almacenar los ítems (nombre, tipo, valor)
        nombre_tabla = []

        # Crear un Frame para el título y el botón
        title_button_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        title_button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Crear y colocar el título del cuadro en el contenedor
        titulo_cuadro = tk.Label(title_button_frame, text=titulo_tabla, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_cuadro.pack(side="left")

        # Crear un botón "Agregar" dentro del contenedor
        button_agregar = tk.Button(title_button_frame, text="Agregar", command=lambda: agregar_item(table_frame, nombre_tabla, simple, medio, complejo))
        button_agregar.pack(side="right")

        # Crear un Frame para la "tabla" dentro del cuadro
        table_frame = tk.Frame(frame_cuadro, bg=COLOR_FONDO)
        table_frame.pack(pady=0, fill="both", expand=True)

        return table_frame, nombre_tabla

    # ------------------------------------------------------------------------------------------

    def agregar_item(table_frame, nombre_tabla, simple, medio, complejo):
        popup = tk.Toplevel(root)
        popup.title("Agregar Entrada")

        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set("Simple")  # Valor predeterminado
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
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_item).grid(row=2, columnspan=2, pady=10)

    def editar_item(table_frame, idx, nombre_tabla, medio, simple, complejo):
        item = nombre_tabla[idx - 1]  # Obtenemos el elemento correspondiente al índice
        nombre_antiguo, tipo_antiguo, _ = item  # Desempaquetamos el elemento

        # Crear la root emergente para la edición
        popup = tk.Toplevel(root)
        popup.title("Editar Entrada")

        # Campos prellenados con los valores antiguos
        tk.Label(popup, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, pady=10)
        nombre_entry = tk.Entry(popup)
        nombre_entry.insert(0, nombre_antiguo)  # Poner el valor antiguo en el campo
        nombre_entry.grid(row=0, column=1, pady=10)

        tk.Label(popup, text="Tipo:", bg=COLOR_FONDO).grid(row=1, column=0, pady=10)
        tipo_var = tk.StringVar(popup)
        tipo_var.set(tipo_antiguo)  # Poner el valor antiguo como seleccionado
        tipo_menu = tk.OptionMenu(popup, tipo_var, "Simple", "Medio", "Complejo")
        tipo_menu.grid(row=1, column=1, pady=10)

        def guardar_edicion():
            nombre_nuevo = nombre_entry.get()
            tipo_nuevo = tipo_var.get()
            if nombre_nuevo:
                valor_nuevo = simple if tipo_nuevo == "Simple" else (medio if tipo_nuevo == "Medio" else complejo)
                nombre_tabla[idx - 1] = (nombre_nuevo, tipo_nuevo, valor_nuevo) # Actualizar la lista con los nuevos valores
                actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
                actualizar_total()
                popup.destroy()

        tk.Button(popup, text="Guardar", command=guardar_edicion).grid(row=2, columnspan=2, pady=10)

    def eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo):
        del nombre_tabla[idx - 1]  # Restamos 1 porque el índice del widget comienza en 1, pero en la lista comienza en 0
        actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo)
        actualizar_total()

    def actualizar_tabla(table_frame, nombre_tabla, simple, medio, complejo):
        # Limpiar la tabla
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Títulos de la tabla
        tk.Label(table_frame, text="Nombre", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=0, column=0, sticky="nsew")
        tk.Label(table_frame, text="Tipo", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=1, sticky="nsew")
        tk.Label(table_frame, text="Valor", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=0, column=2, sticky="nsew")

        # Agregar datos a la tabla
        contador = 0
        contadorFilas = 0
        for i, (nombre, tipo, valor) in enumerate(nombre_tabla, start=1):
            tk.Label(table_frame, text=nombre, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10).grid(row=i, column=0, sticky="nsew")
            tk.Label(table_frame, text=tipo, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8).grid(row=i, column=1, sticky="nsew")
            tk.Label(table_frame, text=valor, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8).grid(row=i, column=2, sticky="nsew")
            # Botones para editar y eliminar el ítem
            editar_button = tk.Button(table_frame, text="Editar", command=lambda idx=i: editar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            editar_button.grid(row=i, column=3)
            eliminar_button = tk.Button(table_frame, text="Eliminar", command=lambda idx=i: eliminar_item(table_frame, idx, nombre_tabla, simple, medio, complejo))
            eliminar_button.grid(row=i, column=4)

            contador += valor
            contadorFilas = i

        # Fila del total
        tk.Label(table_frame, text="TOTAL", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=10, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=0, sticky="nsew")
        tk.Label(table_frame, text="", borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=1, sticky="nsew")
        tk.Label(table_frame, text=contador, borderwidth=1, relief=COLOR_BORDE_INTERNO, width=8, bg=COLOR_ETIQUETA).grid(row=contadorFilas + 1, column=2, sticky="nsew")


    # ----------------------------------------------------------------------------------------
    # Crear un Frame para la sección que ocupe el 40% del tamaño de la root

   
    # ------------------------------------------------------------------------------------------
    def crear_seccion_resultado(titulo):
        frame_seccion = tk.Frame(root, borderwidth=2, relief=COLOR_BORDE, bg=COLOR_FONDO)
        frame_seccion.place(relx=0.36, rely=0.61, relwidth=0.25, relheight=0.15)

        # Título de la sección
        titulo_label = tk.Label(frame_seccion, text=titulo, font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_TITULO)
        titulo_label.pack(pady=10)

        # Etiqueta para el valor del resultado
        valor_resultante = tk.Label(frame_seccion, text="0", font=("Arial", 12), bg=COLOR_FONDO)
        valor_resultante.pack(pady=10)

        return frame_seccion, valor_resultante

    #---------------------------------------------------------------------------------------------

    #Control de los totales

    def actualizar_total():
        total = 0
        for items in [itemsEntradas, itemsSalidas, itemsPeticiones]:
            total += sum(valor for _, _, valor in items)
        resultado_label.config(text=str(total))


    #----------------------------------------------------------------

    table_frame_entradas, itemsEntradas = crear_cuadro("Pantallas", 0.11, 0.01, 1, 2, 3)
    table_frame_salidas, itemsSalidas = crear_cuadro("Reportes", 0.11, 0.31, 2, 5, 8)
    table_frame_peticioines, itemsPeticiones = crear_cuadro("Componentes 3GL", 0.11, 0.61, 5, 7, 10)


    _, resultado_label = crear_seccion_resultado("Puntos de Objetos Totales")


    # Mostrar la tasbla inicialmente
    actualizar_tabla(table_frame_entradas, itemsEntradas)
    actualizar_tabla(table_frame_salidas, itemsSalidas)
    actualizar_tabla(table_frame_peticioines, itemsPeticiones)

    actualizar_total()

def mostrar_acerca_de():
    cambiar_estado_boton(btn_acerca_de)
    # Crear la portada
    portada_frame = tk.Frame(content_frame, bg='white', width=1000, height=800)
    portada_frame.pack(fill='both', expand=True)

    titulo_label = tk.Label(portada_frame, text="Software de la Unidad 3", font=('Helvetica', 36, 'bold'), bg='white')
    titulo_label.pack(pady=40)

    descripcion_texto = """
    Se ha desarrollado todos los métodos y métricas vistas en clase
    """

    descripcion_label = tk.Label(portada_frame, text=descripcion_texto, font=('Helvetica', 18), bg='white', justify='left')
    descripcion_label.pack(padx=100, pady=20)

    equipo_texto = """
    Desarrollado por:
    - Jonathan Oswaldo Castaneda Fabián, CF2014
    - Gerson Alexis Pérez Monterroza, 20072
    """

    equipo_label = tk.Label(portada_frame, text=equipo_texto, font=('Helvetica', 16), bg='white', justify='left')
    equipo_label.pack(pady=20)



# Botones del menú lateral
btn_punto_funcion = tk.Button(menu_frame, text="Puntos de Función", command=puntos_de_funcion)
btn_punto_funcion.pack(fill='x')

btn_casos_usos = tk.Button(menu_frame, text="Casos de Uso", command=casos_de_uso)
btn_casos_usos.pack(fill='x')

btn_punto_objeto = tk.Button(menu_frame, text="Puntos Objeto", command=puntos_objeto)
btn_punto_objeto.pack(fill='x')

btn_acerca_de = tk.Button(menu_frame, text="Acerca de", command=mostrar_acerca_de)
btn_acerca_de.pack(fill='x')

# Etiqueta para mostrar el contenido principal
#content_label = tk.Label(content_frame, text="Bienvenido", font=('Helvetica', 24), bg='white')
#content_label.pack(pady=20)

#Establece el primer boton como activo
cambiar_estado_boton(btn_punto_funcion)
mostrar_acerca_de()

# Iniciar el bucle principal de la aplicación

root.mainloop()

