import tkinter as tk
from tkinter import ttk, messagebox

# Constantes de COCOMO Básico
COCOMO_CONSTANTS = {
    "Orgánico": {"a": 2.4, "b": 1.05, "c": 2.5, "d": 0.38},
    "Semi-Integrado": {"a": 3.0, "b": 1.12, "c": 2.5, "d": 0.35},
    "Empotrado": {"a": 3.6, "b": 1.20, "c": 2.5, "d": 0.32},
}

def calculate_cocomo():
    try:
        kloc = float(entry_kloc.get())
        project_type = combobox_type.get()

        if project_type not in COCOMO_CONSTANTS:
            messagebox.showerror("Error", "Selecciona un tipo de proyecto válido")
            return

        constants = COCOMO_CONSTANTS[project_type]
        effort = constants["a"] * (kloc ** constants["b"])
        time = constants["c"] * (effort ** constants["d"])

        label_result_effort.config(text=f"Esfuerzo estimado: {effort:.2f} persona-meses")
        label_result_time.config(text=f"Tiempo de desarrollo: {time:.2f} meses")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un valor numérico válido para KLOC")

def clear_form1():
    entry_kloc.delete(0, tk.END)
    combobox_type.set("Orgánico")
    label_result_effort.config(text="Esfuerzo estimado: ")
    label_result_time.config(text="Tiempo de desarrollo: ")

def show_form1():
    clear_frame()
    tk.Label(main_frame, text="Estimación de costos con COCOMO", font=('Helvetica', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    
    tk.Label(main_frame, text="Tamaño del proyecto (KLOC):").grid(row=1, column=0, pady=5)
    global entry_kloc
    entry_kloc = tk.Entry(main_frame)
    entry_kloc.grid(row=1, column=1, pady=5)

    tk.Label(main_frame, text="Tipo de proyecto:").grid(row=2, column=0, pady=5)
    global combobox_type
    combobox_type = ttk.Combobox(main_frame, values=["Orgánico", "Semi-Integrado", "Empotrado"])
    combobox_type.grid(row=2, column=1, pady=5)
    combobox_type.set("Orgánico")  # Valor por defecto

    tk.Button(main_frame, text="Calcular", command=calculate_cocomo).grid(row=3, columnspan=2, pady=10)
    tk.Button(main_frame, text="Limpiar Campos", command=clear_form1).grid(row=4, columnspan=2, pady=5)

    global label_result_effort
    global label_result_time
    label_result_effort = tk.Label(main_frame, text="Esfuerzo estimado: ")
    label_result_effort.grid(row=5, columnspan=2, pady=5)
    label_result_time = tk.Label(main_frame, text="Tiempo de desarrollo: ")
    label_result_time.grid(row=6, columnspan=2, pady=5)

def clear_form2():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def show_form2():
    clear_frame()
    tk.Label(main_frame, text="Formulario 2", font=('Helvetica', 14, 'bold')).grid(row=0, columnspan=2, pady=10)
    tk.Label(main_frame, text="Nombre:").grid(row=1, column=0, pady=5)
    global entry_name
    entry_name = tk.Entry(main_frame)
    entry_name.grid(row=1, column=1, pady=5)
    
    tk.Label(main_frame, text="Email:").grid(row=2, column=0, pady=5)
    global entry_email
    entry_email = tk.Entry(main_frame)
    entry_email.grid(row=2, column=1, pady=5)
    
    tk.Button(main_frame, text="Enviar", command=lambda: messagebox.showinfo("Formulario 2", "Datos enviados")).grid(row=3, columnspan=2, pady=10)
    tk.Button(main_frame, text="Limpiar Campos", command=clear_form2).grid(row=4, columnspan=2, pady=5)


def close_app():
    root.quit()

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Menú Profesional")
root.geometry("800x600")

# Crear un frame para los botones del menú
menu_frame = tk.Frame(root, bg='lightgrey', width=150)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Crear un frame principal donde se mostrarán los formularios
main_frame = tk.Frame(root, bg='white')
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear y colocar los botones del menú en el frame del menú
button_form1 = tk.Button(menu_frame, text="COCOMO", command=show_form1)
button_form1.pack(fill=tk.X, padx=10, pady=10)

button_form2 = tk.Button(menu_frame, text="Formulario 2", command=show_form2)
button_form2.pack(fill=tk.X, padx=10, pady=10)

button_form3 = tk.Button(menu_frame, text="Cerrar Programa", command=close_app)
button_form3.pack(fill=tk.X, padx=10, pady=10)

# Iniciar con el primer formulario visible
show_form1()

# Iniciar el bucle principal de la ventana
root.mainloop()
