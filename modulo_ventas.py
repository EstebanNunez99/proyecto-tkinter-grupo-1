import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db_connector  # para que se conecte a la base de datos

def abrir_ventana_nueva_venta():
    ventana_venta = tk.Toplevel()
    ventana_venta.title("Nueva Venta")
    ventana_venta.geometry("800x400")

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

    # =================================
    # == FUNCIÓN "Agregar producto" ===
    #==================================
    def agregar_producto():
        nonlocal total_venta

        nombre = entry_nombre.get()
        cantidad_str = entry_cantidad.get()
        pu_str = entry_pu.get()

        if not nombre:
            messagebox.showwarning("Error de Entrada","El campo 'Nombre' no puede estar vacío", parent=ventana_venta)
            entry_nombre.focus()
            return  
        if not cantidad_str:
            messagebox.showwarning("Error de entrada", "El campo 'Cantidad' no puede estar vacío", parent=ventana_venta)
            entry_cantidad.focus()
            return
        if not pu_str:
            messagebox.showwarning("Error de entrada", "El campo 'PU' no puede estar vacío", parent=ventana_venta)
            entry_pu.focus()
            return
        
        try:
            cantidad = float(cantidad_str)
        except ValueError:
            messagebox.showerror("Error de tipo", "La 'Cantidad' debe ser un número (ej: 1 o 1.5).", parent=ventana_venta)
            entry_cantidad.focus()
            return
        
        try:
            pu = float(pu_str)
        except ValueError:
            messagebox.showerror("Error de tipo", "El 'PU' debe ser un número (ej: 150.50).", parent=ventana_venta)
            entry_cantidad.focus()
            return


        if cantidad <= 0:
            messagebox.showwarning("Error lógico", "La 'Cantidad' debe ser mayor a 0", parent=ventana_venta)
            entry_cantidad.focus()
            return
        if pu <= 0:
            messagebox.showwarning("Error lógico", "El 'PU' debe ser mayor a 0", parent=ventana_venta)
            entry_pu.focus()
            return
        
        subtotal = cantidad * pu

        total_venta += subtotal
        label_total.config(text=f"TOTAL: ${total_venta:.2f}")

        tabla_venta.insert('', tk.END, values=(nombre, cantidad, f"${pu:.2f}", f"${subtotal:.2f}"))

        entry_nombre.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_pu.delete(0, tk.END)
        entry_nombre.focus()



    # =================================
    # == FUNCIÓN "Eliminar producto" ==
    #==================================
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

    
    def finalizar_y_guardar():
        nonlocal total_venta
        
        items_en_tabla = tabla_venta.get_children()
        
        if not items_en_tabla:
            messagebox.showwarning("Venta Vacía", "Agregá productos para crear una venta", parent=ventana_venta)
            return

        lista_productos_para_bd = []
        for item_id in items_en_tabla:
            valores_fila = tabla_venta.item(item_id, "values")
            nombre = valores_fila[0]
            cantidad = float(valores_fila[1])
            # Limpiamos el PU (quitamos "$")
            pu = float(valores_fila[2].replace("$", ""))
            
            lista_productos_para_bd.append((nombre, cantidad, pu))

        # --- Lógica de Hilos para no congelar la App ---
        
        # Deshabilitamos botones para evitar doble click
        boton_agregar.config(state=tk.DISABLED)
        boton_eliminar.config(state=tk.DISABLED)
        boton_guardar.config(state=tk.DISABLED, text="Guardando...")

        # 2. Funciones de Callback (para el hilo)
        def _on_guardado_exitoso():
            # Esta función será llamada por el hilo cuando termine BIEN
            # Usamos 'after' para asegurar que el messagebox corra en el hilo principal
            def lambda_exito():
                try:
                    # Comprueba si la ventana 'ventana_venta' todavía existe
                    if ventana_venta.winfo_exists():
                        messagebox.showinfo("Éxito", "Venta guardada correctamente.", parent=ventana_venta)
                        ventana_venta.destroy()
                except tk.TclError:
                    # La ventana fue destruida mientras esperábamos
                    print("Ventana de venta cerrada antes de mostrar éxito.")

            ventana_venta.after(0, lambda_exito)

        def _on_guardado_error(error_msg):
            # Esta función será llamada por el hilo si ALGO FALLA
            def lambda_error():
                # Comprueba si la ventana 'ventana_venta' todavía existe
                try:
                    if ventana_venta.winfo_exists():
                        messagebox.showerror("Error de Base de datos", f"No se pudo guardar la venta:\n{error_msg}", parent=ventana_venta)
                        # Rehabilitamos botones para que pueda reintentar
                        boton_agregar.config(state=tk.NORMAL),
                        boton_eliminar.config(state=tk.NORMAL),
                        boton_guardar.config(state=tk.NORMAL, text="Finalizar y Guardar")
                except tk.TclError:
                    print("Ventana de venta cerrada antes de mostrar error.")

            ventana_venta.after(0, lambda_error),
                
        
        # 3. Llamamos a la función del conector EN HILO
        db_connector.guardar_venta_en_hilo(
            lista_productos=lista_productos_para_bd,
            total_venta=total_venta,
            callback_exito=_on_guardado_exitoso,
            callback_error=_on_guardado_error
        )
    
    
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


    # --- Scrollbar ---
    scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla_venta.yview)
    tabla_venta.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabla_venta.pack(fill=tk.BOTH, expand=True)

    # Botones de Acción y Total
    boton_agregar = tk.Button(frame_botones, text="Agregar producto", command=agregar_producto)
    boton_agregar.pack(side=tk.LEFT, padx=10)

    boton_eliminar = tk.Button(frame_botones, text="Eliminar producto", command=eliminar_producto)
    boton_eliminar.pack(side=tk.LEFT, padx=10)
    
    boton_guardar = tk.Button(
        frame_botones, 
        text="Finalizar y Guardar", 
        command=finalizar_y_guardar,
        font=("Arial", 10, "bold"),
        bg="#4CAF50", # Un color verde
        fg="white"
    )
    boton_guardar.pack(side=tk.LEFT, padx=5)

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

#Ahora ya no necesitamos, porque creé el nuevo punto de entrada main.py
#este archivo ahora solo es un modulo
# if __name__ == "__main__":

#     ventana_principal_prueba = tk.Tk()
#     ventana_principal_prueba.title("Ventana de Prueba(Proyecto Grande)")

#     boton_prueba = tk.Button(ventana_principal_prueba, text="Abrir Módulo de 'Nueva Venta'", command=abrir_ventana_nueva_venta)

#     boton_prueba.pack(expand=True, padx=50, pady=30)

#     ventana_principal_prueba.mainloop()
    