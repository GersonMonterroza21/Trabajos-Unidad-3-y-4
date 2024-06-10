import tkinter as tk
from tkinter import ttk, messagebox

# Definición de las constantes y factores de escala
factores_escala = {
    "PREC": 1.00,  # Precisión requerida
    "FLEX": 1.00,  # Flexibilidad de desarrollo
    "RESL": 1.00,  # Resolución arquitectónica
    "TEAM": 1.00,  # Cohesión del equipo
    "PMAT": 1.00   # Madurez del proceso
}

# Definición de los multiplicadores de esfuerzo
multiplicadores_esfuerzo = {
    "RELY": 1.00,  # Fiabilidad requerida del software
    "DATA": 1.00,  # Tamaño de la base de datos
    "CPLX": 1.00,  # Complejidad del producto
    "RUSE": 1.00,  # Reutilización del software
    "TIME": 1.00,  # Restricciones de tiempo de ejecución
    "STOR": 1.00,  # Restricciones de almacenamiento
    "PVOL": 1.00,  # Volatilidad de la plataforma
    "ACAP": 1.00,  # Capacidad del analista
    "PCAP": 1.00,  # Capacidad del programador
    "PCON": 1.00,  # Continuidad del personal
    "APEX": 1.00,  # Experiencia en aplicaciones
    "PLEX": 1.00,  # Experiencia en la plataforma
    "LTEX": 1.00,  # Experiencia en el lenguaje y herramientas
    "TOOL": 1.00,  # Uso de herramientas de software
    "SITE": 1.00,  # Capacidad del sitio de desarrollo
    "SCED": 1.00   # Cronograma requerido
}

COCOMO_CONSTANTS = {
    "Orgánico": {"a": 2.4, "b": 1.05, "c": 2.5, "d": 0.38},
    "Semi-Integrado": {"a": 3.0, "b": 1.12, "c": 2.5, "d": 0.35},
    "Empotrado": {"a": 3.6, "b": 1.20, "c": 2.5, "d": 0.32},
}

# Constantes del modelo COCOMO II
B = 0.91
A = 2.94

def calcular_esfuerzo():
    try:
        kloc = float(entry_kloc.get())
        if kloc <= 0:
            raise ValueError("KLOC debe ser un valor positivo")
        
        # Leer factores de escala
        escala_factors = [float(entry_vars[factor].get()) for factor in factores_escala]
        escala_producto = B + 0.01 * sum(escala_factors)
        
        # Leer multiplicadores de esfuerzo
        esfuerzo_factors = [float(entry_vars[factor].get()) for factor in multiplicadores_esfuerzo]
        esfuerzo_producto = 1
        for factor in esfuerzo_factors:
            esfuerzo_producto *= factor

        # Calcular el esfuerzo
        esfuerzo = A * (kloc ** escala_producto) * esfuerzo_producto
        label_result.config(text=f"Esfuerzo estimado: {esfuerzo:.2f} Persona-Meses")
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

def clear_form2():
    entry_kloc.delete(0, tk.END)
    for var in entry_vars.values():
        var.set("1.00")
    label_result.config(text="Esfuerzo estimado: ")

def show_form1():
    clear_frame()
    tk.Label(main_frame, text="Estimación de costos con COCOMO", font=('Helvetica', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    tk.Label(main_frame, text="Tamaño del proyecto (KLOC):").grid(row=1, column=0, pady=5)
    global entry_kloc1
    entry_kloc1 = tk.Entry(main_frame)
    entry_kloc1.grid(row=1, column=1, pady=5)

    tk.Label(main_frame, text="Tipo de proyecto:").grid(row=2, column=0, pady=5)
    global combobox_type
    combobox_type = ttk.Combobox(main_frame, values=["Orgánico", "Semi-Integrado", "Empotrado"])
    combobox_type.grid(row=2, column=1, pady=5)
    combobox_type.set("Orgánico")  # Valor por defecto
    
    button_calcular = ttk.Button(main_frame, text="Calcular", command=calculate_cocomo1)
    button_calcular.grid(row=3, column=0, pady=10, padx=(0, 5))

    button_limpiar = ttk.Button(main_frame, text="Limpiar Campos", command=clear_form1)
    button_limpiar.grid(row=3, column=1, pady=10, padx=(5, 0))

   
    global label_result_effort1
    global label_result_time1
    label_result_effort1 = tk.Label(main_frame, text="Esfuerzo estimado: ")
    label_result_effort1.grid(row=5, columnspan=2, pady=5)
    label_result_time1 = tk.Label(main_frame, text="Tiempo de desarrollo: ")
    label_result_time1.grid(row=6, columnspan=2, pady=5)

def calculate_cocomo1():
    try:
        kloc = float(entry_kloc1.get())
        project_type = combobox_type.get()

        if project_type not in COCOMO_CONSTANTS:
            messagebox.showerror("Error", "Selecciona un tipo de proyecto válido")
            return

        constants = COCOMO_CONSTANTS[project_type]
        effort = constants["a"] * (kloc ** constants["b"])
        time = constants["c"] * (effort ** constants["d"])

        label_result_effort1.config(text=f"Esfuerzo estimado: {effort:.2f} persona-meses")
        label_result_time1.config(text=f"Tiempo de desarrollo: {time:.2f} meses")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un valor numérico válido para KLOC")

def clear_form1():
    entry_kloc1.delete(0, tk.END)
    combobox_type.set("Orgánico")
    label_result_effort1.config(text="Esfuerzo estimado: ")
    label_result_time1.config(text="Tiempo de desarrollo: ")

def show_form2():
    clear_frame()
    
    tk.Label(main_frame, text="Calculadora COCOMO II", font=('Helvetica', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    # Frame para KLOC
    frame_kloc = ttk.Frame(main_frame, padding="10 10 10 10")
    frame_kloc.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    ttk.Label(frame_kloc, text="Ingrese el número de KLOC:").grid(column=0, row=0, padx=5, pady=5, sticky="e")
    global entry_kloc
    entry_kloc = ttk.Entry(frame_kloc)
    entry_kloc.grid(column=1, row=0, padx=5, pady=5, sticky="w")

    # Frame para los factores de escala
    frame_escala = ttk.LabelFrame(main_frame, text="Factores de Escala", padding="10 10 10 10")
    frame_escala.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    global entry_vars
    entry_vars = {}

    for i, factor in enumerate(factores_escala):
        ttk.Label(frame_escala, text=factor).grid(column=0, row=i, padx=5, pady=5, sticky="e")
        entry_vars[factor] = tk.StringVar(value="1.00")
        entry = ttk.Entry(frame_escala, textvariable=entry_vars[factor])
        entry.grid(column=1, row=i, padx=5, pady=5, sticky="w")

    # Frame para los multiplicadores de esfuerzo
    frame_esfuerzo1 = ttk.LabelFrame(main_frame, text="Multiplicadores de Esfuerzo (Parte 1)", padding="10 10 10 10")
    frame_esfuerzo1.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Frame para los multiplicadores de esfuerzo (segunda parte)
    frame_esfuerzo2 = ttk.LabelFrame(main_frame, text="Multiplicadores de Esfuerzo (Parte 2)", padding="10 10 10 10")
    frame_esfuerzo2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    # Separar los multiplicadores en dos grupos
    multiplicadores_keys = list(multiplicadores_esfuerzo.keys())
    mid = len(multiplicadores_keys) // 2
    multiplicadores_esfuerzo1 = multiplicadores_keys[:mid]
    multiplicadores_esfuerzo2 = multiplicadores_keys[mid:]

    for i, factor in enumerate(multiplicadores_esfuerzo1):
        ttk.Label(frame_esfuerzo1, text=factor).grid(column=0, row=i, padx=5, pady=5, sticky="e")
        entry_vars[factor] = tk.StringVar(value="1.00")
        entry = ttk.Entry(frame_esfuerzo1, textvariable=entry_vars[factor])
        entry.grid(column=1, row=i, padx=5, pady=5, sticky="w")

    for i, factor in enumerate(multiplicadores_esfuerzo2):
        ttk.Label(frame_esfuerzo2, text=factor).grid(column=0, row=i, padx=5, pady=5, sticky="e")
        entry_vars[factor] = tk.StringVar(value="1.00")
        entry = ttk.Entry(frame_esfuerzo2, textvariable=entry_vars[factor])
        entry.grid(column=1, row=i, padx=5, pady=5, sticky="w")

    # Botones para calcular el esfuerzo y limpiar campos
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=3, column=0, columnspan=3, pady=10)

    button_calcular = ttk.Button(button_frame, text="Calcular Esfuerzo", command=calcular_esfuerzo)
    button_calcular.pack(side=tk.LEFT, padx=5)

    button_limpiar = ttk.Button(button_frame, text="Limpiar Campos", command=clear_form2)
    button_limpiar.pack(side=tk.LEFT, padx=5)

    # Etiqueta para mostrar el resultado
    global label_result
    label_result = ttk.Label(main_frame, text="Esfuerzo estimado: ")
    label_result.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


def show_form3():
    clear_frame()
    tk.Label(main_frame, text="Cerrar Programa", font=('Helvetica', 14, 'bold')).grid(row=0, columnspan=3, pady=10)
    tk.Button(main_frame, text="Cerrar", command=close_app).grid(row=1, columnspan=3, pady=10)

def close_app():
    root.quit()

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Menú Profesional")
root.geometry("1000x600")

# Crear un frame para los botones del menú
menu_frame = tk.Frame(root, bg='lightgrey', width=150)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Crear un frame principal donde se mostrarán los formularios
main_frame = tk.Frame(root, bg='white')
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear y colocar los botones del menú en el frame del menú
button_form1 = tk.Button(menu_frame, text="COCOMO", command=show_form1)
button_form1.pack(fill=tk.X, padx=10, pady=10)

button_form2 = tk.Button(menu_frame, text="COCOMO II", command=show_form2)
button_form2.pack(fill=tk.X, padx=10, pady=10)

button_form3 = tk.Button(menu_frame, text="Cerrar Programa", command=show_form3)
button_form3.pack(fill=tk.X, padx=10, pady=10)

# Iniciar con el primer formulario visible
show_form1()

# Iniciar el bucle principal de la ventana
root.mainloop()
