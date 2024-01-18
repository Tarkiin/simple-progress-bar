import tkinter as tk
from tkinter import ttk
import time

# Crear la ventana principal
window = tk.Tk()
window.title("Barra de Progreso")

# Quitar la barra de título y los botones de minimizar, maximizar y cerrar
window.overrideredirect(True)

# Crear el label con el mensaje
label = tk.Label(window, text="Cargando aplicación...", font=("Helvetica", 14, "bold"))
label.pack()

# Crear la barra de progreso
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode='determinate')
progress.pack()

# Crear un label para mostrar el porcentaje
percentage_label = tk.Label(window, text="0%", font=("Helvetica", 12, "bold"))
percentage_label.pack()

# Centrar la ventana en la pantalla
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry("+{}+{}".format(position_right, position_down))

# Actualizar la ventana para que se ajuste al tamaño de la barra de progreso
window.update()

# Variable global que representa el progreso total inicial
progress_value = 0


# Función para actualizar la barra de progreso y el label de porcentaje
def update_progress(add_value):
    global progress_value
    progress_value += add_value
    progress['value'] = progress_value
    percentage = progress_value  # Asumiendo que el máximo valor de progress es 100
    percentage_label.config(text=f"{percentage}%")  # Actualizar el texto del label
    window.update()  # Esto es necesario para que se actualice la barra de progreso inmediatamente


# Simulación de progreso
for i in range(100):
    update_progress(1)
    time.sleep(0.02)

# Cerrar la ventana automáticamente al completar la barra de progreso
window.destroy()
