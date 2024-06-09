import tkinter as tk
from tkinter import ttk, messagebox

# Constantes de COCOMO Básico
constantes_cocomo = {
    "Orgánico": {"a": 2.4, "b": 1.05, "c": 2.5, "d": 0.38},
    "Semi-Integrado": {"a": 3.0, "b": 1.12, "c": 2.5, "d": 0.35},
    "Empotrado": {"a": 3.6, "b": 1.20, "c": 2.5, "d": 0.32},
}

def calcular_cocomo():
    try:
        kloc = float(entry_kloc.get())
        project_type = combobox_type.get()

        if project_type not in constantes_cocomo:
            messagebox.showerror("Error", "Selecciona un tipo de proyecto válido")
            return

        constantes = constantes_cocomo[project_type]
        esfuerzo = constantes["a"] * (kloc ** constantes["b"])
        tiempo = constantes["c"] * (esfuerzo ** constantes["d"])

        label_resultado_esfuerzo.config(text=f"Esfuerzo estimado: {esfuerzo:.2f} persona-meses")
        label_resultado_tiempo.config(text=f"Tiempo de desarrollo: {tiempo:.2f} meses")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un valor numérico válido para KLOC")

# Crear la ventana principal
root = tk.Tk()
root.title("Estimación de costos con COCOMO")

# Crear y colocar las etiquetas y campos de entrada
label_kloc = tk.Label(root, text="Tamaño del proyecto (KLOC):")
label_kloc.grid(row=0, column=0, padx=10, pady=10)
entry_kloc = tk.Entry(root)
entry_kloc.grid(row=0, column=1, padx=10, pady=10)

label_type = tk.Label(root, text="Tipo de proyecto:")
label_type.grid(row=1, column=0, padx=10, pady=10)
combobox_type = ttk.Combobox(root, values=["Orgánico", "Semi-Integrado", "Empotrado"])
combobox_type.grid(row=1, column=1, padx=10, pady=10)
combobox_type.set("Orgánico")  # Valor por defecto

# Crear y colocar el botón de calcular
boton_calcular = tk.Button(root, text="Calcular", command=calcular_cocomo)
boton_calcular.grid(row=2, columnspan=2, pady=10)

# Etiquetas para mostrar los resultados
label_resultado_esfuerzo = tk.Label(root, text="Esfuerzo estimado: ")
label_resultado_esfuerzo.grid(row=3, columnspan=2, pady=5)
label_resultado_tiempo = tk.Label(root, text="Tiempo de desarrollo: ")
label_resultado_tiempo.grid(row=4, columnspan=2, pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
