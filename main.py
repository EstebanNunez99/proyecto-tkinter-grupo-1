import tkinter as tk
from tkinter import ttk 
import RELOJ # este es el modulo RELOJ hecho por Lorena



ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Kiosco - Proyecto Grupal")
ventana_principal.geometry("600x400")

# --- Contenedor para el Reloj (arriba) ---
# Ahora hacemos que este frame combine con el fondo del reloj
frame_superior = tk.Frame(ventana_principal, bg="pink")
frame_superior.pack(fill=tk.X, side=tk.TOP, pady=5)

# --- Contenedor para los Botones (centro) ---
frame_central = tk.Frame(ventana_principal)
frame_central.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


RELOJ.crear_reloj(frame_superior)



estilo_botones = ttk.Style()
estilo_botones.configure("TButton", font=("Arial", 12, "bold"), padding=15)

boton_nueva_venta = ttk.Button(
    frame_central, 
    text="Registrar Nueva Venta",
    style="TButton"
)
boton_nueva_venta.pack(fill=tk.X, pady=10)

boton_panel_ventas = ttk.Button(
    frame_central, 
    text="Abrir Panel de Ventas",
    style="TButton"
)
boton_panel_ventas.pack(fill=tk.X, pady=10)


ventana_principal.mainloop()