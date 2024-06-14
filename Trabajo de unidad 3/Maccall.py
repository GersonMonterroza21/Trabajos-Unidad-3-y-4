import tkinter as tk
from tkinter import ttk, messagebox

class McCallApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(" Calidad de McCall")
        self.geometry("1150x700")
        self.configure(bg="#D6EAF8")  # Color de fondo celeste claro
        
        self.metricas = {
            "Operación del Producto": {
                "Corrección": ["Exactitud", "Compleción"],
                "Confiabilidad": ["Madurez", "Tolerancia a fallos", "Recuperabilidad"],
                "Eficiencia": ["Tiempo de ejecución", "Uso de recursos"],
                "Integridad": ["Control de acceso", "Protección de datos"],
                "Usabilidad": ["Facilidad de uso", "Capacidad de entrenamiento"]
            },
            "Revisión del Producto": {
                "Mantenibilidad": ["Facilidad de análisis", "Facilidad de cambio"],
                "Flexibilidad": ["Modularidad", "Adaptabilidad"],
                "Testabilidad": ["Facilidad de prueba"]
            },
            "Transición del Producto": {
                "Portabilidad": ["Adaptabilidad", "Sustitución"],
                "Reusabilidad": ["Generalidad", "Independencia de software"],
                "Interoperabilidad": ["Compatibilidad", "Capacidad de comunicación"]
            }
        }
        
        self.puntuaciones = {}
        self.resultados_labels = {}
        self.crear_widgets()
    
    def crear_widgets(self):
        contenedor_principal = tk.Frame(self, bg="#D6EAF8")  # Color de fondo celeste claro
        contenedor_principal.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(contenedor_principal, bg="#D6EAF8", highlightthickness=0)  # Sin borde de resaltado
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(contenedor_principal, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        contenedor_interior = tk.Frame(canvas, bg="#D6EAF8")  # Color de fondo celeste claro
        canvas.create_window((0, 0), window=contenedor_interior, anchor="nw")
        
        fila = 0
        for factor, submetricas in self.metricas.items():
            factor_frame = ttk.LabelFrame(contenedor_interior, text=factor, padding=(10, 10), relief="groove")
            factor_frame.grid(row=0, column=fila, padx=10, pady=10, sticky="n")
            fila += 1
            
            subfila = 0
            for subfactores, items in submetricas.items():
                ttk.Label(factor_frame, text=f"{subfactores}:", font=('Arial', 12), anchor="w").grid(column=0, row=subfila, padx=10, pady=5, sticky=tk.W)
                subfila += 1
                for item in items:
                    ttk.Label(factor_frame, text=f"  {item}:", anchor="w").grid(column=0, row=subfila, padx=20, pady=5, sticky=tk.W)
                    combobox = ttk.Combobox(factor_frame, values=[i for i in range(11)], width=5, justify="center")
                    combobox.grid(column=1, row=subfila, padx=10, pady=5)
                    combobox.set(0)  # Establecer el valor por defecto en 0
                    self.puntuaciones[item] = combobox
                    subfila += 1
        
        # Botón "Calcular Puntuación de Calidad" al lado del botón "Cerrar"
        ttk.Button(contenedor_interior, text="Calcular Puntuación de Calidad", command=self.calcular_calidad).grid(row=subfila, column=0, pady=20, padx=10, sticky="w")
        ttk.Button(contenedor_interior, text="Cerrar", command=self.destroy).grid(row=subfila, column=1, pady=20, padx=10, sticky="e")
        
        subfila += 1
        
        # Labels para mostrar los resultados debajo de las últimas dos tablas
        resultados_frame = ttk.LabelFrame(contenedor_interior, text="Resultados", padding=(10, 10), relief="groove")
        resultados_frame.grid(row=subfila, columnspan=fila, padx=10, pady=10, sticky="we")
        
        self.resultados_labels["Operación del Producto"] = ttk.Label(resultados_frame, text="", font=('Arial', 12), anchor="w")
        self.resultados_labels["Operación del Producto"].grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.resultados_labels["Revisión del Producto"] = ttk.Label(resultados_frame, text="", font=('Arial', 12), anchor="w")
        self.resultados_labels["Revisión del Producto"].grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.resultados_labels["Transición del Producto"] = ttk.Label(resultados_frame, text="", font=('Arial', 12), anchor="w")
        self.resultados_labels["Transición del Producto"].grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        contenedor_interior.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
    def calcular_calidad(self):
        try:
            factor_puntuaciones = {
                "Operación del Producto": [],
                "Revisión del Producto": [],
                "Transición del Producto": []
            }
            
            for factor, submetricas in self.metricas.items():
                for subfactores, items in submetricas.items():
                    for item in items:
                        puntuacion = self.puntuaciones[item].get()
                        if not puntuacion.isdigit() or int(puntuacion) < 0 or int(puntuacion) > 10:
                            raise ValueError(f"La puntuación para {item} debe estar entre 0 y 10.")
                        factor_puntuaciones[factor].append(int(puntuacion))
            
            resultados = {}
            for factor, puntuaciones in factor_puntuaciones.items():
                promedio = sum(puntuaciones) / len(puntuaciones)
                resultados[factor] = f"{promedio:.1f}/10"
                self.resultados_labels[factor].configure(text=f"{factor}: {resultados[factor]}")
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = McCallApp()
    app.mainloop()
