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
    for boton in [btn_nuevo, btn_abrir, btn_guardar, btn_acerca_de]:
        boton.config(bg='SystemButtonFace')

    boton_activado.config(bg='lightblue')

def puntos_de_funcion():
    cambiar_estado_boton(btn_nuevo)
    content_label.config(text="Puntos de Función")

def casos_de_uso():
    cambiar_estado_boton(btn_abrir)
    content_label.config(text="Casos de Uso")

def puntos_objeto():
    cambiar_estado_boton(btn_guardar)
    content_label.config(text="Puntos Objeto")

def mostrar_acerca_de():
    cambiar_estado_boton(btn_acerca_de)
    content_label.config(text="Acerca de la Aplicación")

btn_nuevo = tk.Button(menu_frame, text="Puntos de Función", command=puntos_de_funcion)
btn_nuevo.pack(fill='x')

btn_abrir = tk.Button(menu_frame, text="Casos de Uso", command=casos_de_uso)
btn_abrir.pack(fill='x')

btn_guardar = tk.Button(menu_frame, text="Puntos Objeto", command=puntos_objeto)
btn_guardar.pack(fill='x')

btn_acerca_de = tk.Button(menu_frame, text="Acerca de", command=mostrar_acerca_de)
btn_acerca_de.pack(fill='x')

content_label = tk.Label(content_frame, text="Bienvenido", font=('Helvetica', 24), bg='white')
content_label.pack(pady=20)

cambiar_estado_boton(btn_nuevo)  # Establecer el primer botón como activo inicialmente

root.mainloop()
