import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def abrir_ventana_nueva_venta():
    ventana_venta = tk.Toplevel()
    ventana_venta.title("Nueva Venta")
    ventana_venta.geometry("600x500")

    total_venta = 0.0
    
    # Contenedor para los campos de entrada
    frame_entradas = tk.Frame(ventana_venta, padx=10, pady=10)
    frame_entradas.pack(fill=tk.X)

    # Contenedor para la tabla
    frame_tabla = tk.Frame(ventana_venta, padx=10, pady=5)
    frame_tabla.pack(fill=tk.BOTH, expand=True)

    # Contenedor para los botones de abajo
    frame_botones = tk.Frame(ventana_venta, padx=10, pady=10)
    frame_botones.pack(fill=tk.X, side=tk.BOTTOM)

    # --- Entradas de datos ---
    tk.Label(frame_entradas, text="Nombre:").grid(row=0, column=0, padx=5)
    entry_nombre = tk.Entry(frame_entradas)
    entry_nombre.grid(row=0, column=1, padx=5)

    tk.Label(frame_entradas, text="Cantidad:").grid(row=0, column=2, padx=5)
    entry_cantidad = tk.Entry(frame_entradas, width=10)
    entry_cantidad.grid(row=0, column=3, padx=5)

    tk.Label(frame_entradas, text="Precio Unitario (PU):").grid(row=0, column=4, padx=5)
    entry_pu = tk.Entry(frame_entradas, width=10)
    entry_pu.grid(row=0, column=5, padx=5)

    # --- Lógica de la tabla (Funciones anidadas) ---
    def agregar_producto():
        nonlocal total_venta
        try:
            nombre = entry_nombre.get()
            cantidad = int(entry_cantidad.get())
            pu = float(entry_pu.get())

            if not nombre or cantidad <= 0 or pu <= 0:
                messagebox.showwarning("Datos incompletos", "Por favor, ingrese todos los datos.", parent=ventana_venta)
                return
            
            subtotal = cantidad * pu

            # Actualizar total
            total_venta+= subtotal
            label_total.config(text=f"TOTAL: ${total_venta:.2F}")

            # Insertar en la tabla
            tabla_venta.insert('', tk.END, values=(nombre, cantidad, f"${pu:.2f}", f"${subtotal:.2f}"))

            # Limpiar campos
            entry_nombre.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            entry_pu.delete(0, tk.END)
            entry_pu.focus()
            entry_nombre.focus()
        
        except ValueError:
            messagebox.showerror("Error de tipo", "Ingrese números válidos en Cantidad y PU.", parent=ventana_venta)
    
    def eliminar_producto():
        nonlocal total_venta
        try:
            seleccion = tabla_venta.selection()
            if not seleccion:
                messagebox.showwarning("Sin selección", "Seleccione un producto para eliminar.", parent=ventana_venta)
                return
            item_seleccionado = seleccion[0]

            # Obtener valores de la fila a eliminar
            valores_fila = tabla_venta.item(item_seleccionado, "values")
            # El subtotal es el 4to valor (índice 3)
            subtotal_a_restar_str = valores_fila[3]
            # Limpiar (quitar "$") y convertir a número
            subtotal_a_restar = float(subtotal_a_restar_str.replace("$", ""))

            # Restar del total y actualizar etiqueta
            total_venta -= subtotal_a_restar
            label_total.config(text=f"TOTAL: ${total_venta:.2f}")

            # Eliminar la fila de la tabla
            tabla_venta.delete(item_seleccionado)
        except:
            messagebox.showerror("Error", "No se pudo eliminar el producto.", parent=ventana_venta)

    # --- Configuración de la Tabla (Treeview) ---
    columnas = ("nombre", "cantidad", "pu", "subtotal")
    tabla_venta = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

    # Columnas
    tabla_venta.heading("nombre", text="Nombre")
    tabla_venta.column("nombre", width=200)
    tabla_venta.heading("cantidad", text="Cantidad")
    tabla_venta.column("cantidad", width=100, anchor=tk.CENTER)
    tabla_venta.heading("pu", text="PU")
    tabla_venta.column("pu", width=100, anchor=tk.E)
    tabla_venta.heading("subtotal", text="Subtotal")
    tabla_venta.column("subtotal", width=100, anchor=tk.E)

    tabla_venta.pack(fill=tk.BOTH, expand=True)

    # --- Scrollbar ---
    scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla_venta.yview)
    tabla_venta.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Botones de Acción y Total
    boton_agregar = tk.Button(frame_botones, text="Agregar producto", command=agregar_producto)
    boton_agregar.pack(side=tk.LEFT, padx=10)

    boton_eliminar = tk.Button(frame_botones, text="Eliminar producto", command=eliminar_producto)
    boton_eliminar.pack(side=tk.LEFT, padx=10)

    # Etiqueta para el Total General
    label_total = tk.Label(frame_botones, text="TOTAL: $0.00", font =("Arial", 14, "bold"))
    label_total.pack(side=tk.RIGHT, padx=20)

    # ---Bloqueo de Ventana---
    ventana_venta.transient()
    ventana_venta.grab_set()
    ventana_venta.wait_window()


# =====================================================
# BLOQUE DE PRUEBA (SOLO PARA PROBAR ESTE ARCHIVO)
# =====================================================

if __name__ == "__main__":

    ventana_principal_prueba = tk.Tk()
    ventana_principal_prueba.title("Ventana de Prueba(Proyecto Grande)")

    tk.Label(ventana_principal_prueba, text="Esta es la ventana principal de tu proyecto.")

    boton_prueba = tk.Button(ventana_principal_prueba, text="Abrir Módulo de 'Nueva Venta'", command=abrir_ventana_nueva_venta)

    boton_prueba.pack(expand=True, padx=50, pady=30)

    ventana_principal_prueba.mainloop()
    