import tkinter as tk
from tkinter import ttk 

import RELOJ # este es el modulo RELOJ hecho por Lorena
import modulo_ventas # este es el modulo_ventas que hizo 
import Proyecto_grupal_Tkinter as panel_ventas # este es el panel de ventas que hizo 

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

def abrir_modulo_ventas():
    boton_nueva_venta.config(state=tk.DISABLED)
    boton_panel_ventas.config(state=tk.DISABLED)

    modulo_ventas.abrir_ventana_nueva_venta()

    boton_nueva_venta.config(state=tk.NORMAL)
    boton_panel_ventas.config(state=tk.NORMAL)

def abrir_modulo_panel():
    boton_nueva_venta.config(state=tk.DISABLED)
    boton_panel_ventas.config(state=tk.DISABLED)

    panel_ventas.abrir_panel()

    boton_nueva_venta.config(state=tk.NORMAL)
    boton_panel_ventas.config(state=tk.NORMAL)



estilo_botones = ttk.Style()
estilo_botones.configure("TButton", font=("Arial", 12, "bold"), padding=15)

boton_nueva_venta = ttk.Button(
    frame_central, 
    text="Registrar Nueva Venta",
    style="TButton",
    #conecto el botón
    command=abrir_modulo_ventas
)
boton_nueva_venta.pack(fill=tk.X, pady=10)

boton_panel_ventas = ttk.Button(
    frame_central, 
    text="Abrir Panel de Ventas",
    style="TButton",
    #conecto el boton
    command=abrir_modulo_panel
)
boton_panel_ventas.pack(fill=tk.X, pady=10)


ventana_principal.mainloop()