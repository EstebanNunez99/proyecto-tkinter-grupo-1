import tkinter as tk
from tkinter import ttk
import db_connector
from tkinter import messagebox
#Ya no necesitamos ahora solo será un modulo
# ventana = tk.Tk()
#Agrego todo a una sola funcion 

#Agrego una funcion para mostrar el historial de ventas
def mostrar_historial_ventas(ventana_padre):

    ventana_historial = tk.Toplevel(ventana_padre)
    ventana_historial.title("Historial de Ventas")
    ventana_historial.geometry("500x400")

    frame_tabla = tk.Frame(ventana_historial)
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    columnas = ("id_venta", "fecha", "total")
    tabla_historial = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    # Columnas
    tabla_historial.heading("id_venta", text="ID Venta")
    tabla_historial.column("id_venta", width=80, anchor=tk.CENTER)
    tabla_historial.heading("fecha", text="Fecha y Hora")
    tabla_historial.column("fecha", width=200)
    tabla_historial.heading("total", text="Total Vendido")
    tabla_historial.column("total", width=100, anchor=tk.E)

    #barra de desplz
    scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla_historial.yview)
    tabla_historial.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabla_historial.pack(fill=tk.BOTH, expand=True)


    id_temporal = tabla_historial.insert('', tk.END, values=("Cargando...", "", ""))
    tabla_historial.configure(selectmode="none") 

    def _on_historial_cargado(historial):
        """Callback que se ejecuta cuando el hilo de BD termina."""
        
        # Corremos la actualización en el hilo principal con 'after'
        def actualizar_tabla():
            tabla_historial.delete(id_temporal)
            tabla_historial.configure(selectmode="browse") 
            
            if not historial:
                tabla_historial.insert('', tk.END, values=("No hay ventas", "", ""))
                return

            # Poblamos la tabla con los datos reales
            for venta in historial:
                id_venta = venta[0]
                fecha = venta[1].strftime('%Y-%m-%d %H:%M:%S') 
                total = f"${venta[2]:.2f}" 
                tabla_historial.insert('', tk.END, values=(id_venta, fecha, total))

        ventana_historial.after(0, actualizar_tabla)


    db_connector.obtener_historial_en_hilo(callback=_on_historial_cargado)

    ventana_historial.transient()
    ventana_historial.grab_set()
    ventana_historial.wait_window()
    
def abrir_panel():
    
    ventana = tk.Toplevel()
    ventana.title ("Trabajo Grupo 1")
    ventana.geometry ("800x400")

    def Trabajo():
        print("Este botón todavia no hace nada :)")
        
        
    def mostrar_info_proyecto():
        titulo = "Acerca del Proyecto"
        info = (
            "Proyecto Grupal - Punto de Venta Básico\n\n"
            "Objetivo:\n"
            "Unificar 4 mini-proyectos "
            "en un solo proyecto. Como extra lo conectamos a una "
            "base de datos PostgreSQL en la nube (Render) para "
            "la persistencia de datos"
        )
        # El 'parent=ventana' asegura que la alerta 
        # aparezca sobre esta ventana
        messagebox.showinfo(titulo, info, parent=ventana)

    def mostrar_info_app():
        titulo = "Acerca de esta APP"
        info = (
            "Gestión de Kiosco v1.0\n\n"
            "Tecnologías usadas:\n"
            " - Python 3\n"
            " - Tkinter (para la GUI)\n"
            " - Psycopg2 (Conector de BD)\n"
            " - PostgreSQL (Hosteado en Render)\n"
            " - Threading (para evitar congelamiento)\n"
            " - Python-dotenv (para variables de entorno)"
        )
        messagebox.showinfo(titulo, info, parent=ventana)
        
    etiqueta = tk.Label(ventana, text="Panel de Ventas", font=("Elephant", 25))
    etiqueta.pack()

    boton1 = tk.Button(ventana, text="Historial de Ventas", font=("Arial Black", 12), command=lambda: mostrar_historial_ventas(ventana))
    boton1.pack()
    boton2 = tk.Button(ventana, text= "Número de Cliente", font=("Arial Black", 12), command= Trabajo)
    boton2.pack()
    boton3 = tk.Button(ventana, text="Devolución de Gastos Personales", font=("Arial Black", 12), command= Trabajo)
    boton3.pack()
    boton4 = tk.Button(ventana, text="Comparación c/ Periodos Anteriores", font=("Arial Black", 12), command= Trabajo)
    boton4.pack()
    boton5 = tk.Button(ventana, text="Cumplimiento de Metas", font=("Arial Black", 12), command= Trabajo)
    boton5.pack()
    boton6 = tk.Button(ventana, text="Gráficos y Visualizaciones", font=("Arial Black", 12), command= Trabajo)
    boton6.pack()

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label ="Vendedor", menu=menu_principal)

    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label ="Registro Unico", menu=submenu)

    submenu.add_command(label = 'Nombre y Apellido')
    submenu.add_command(label = 'Numero De DNI')

    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label ="Nivel de Desempeño", menu=menu_principal)
    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label ="Nivel Actual", menu=submenu)

    submenu.add_command(label = 'Sujeto a Ventas Actuales o Periódicas')


    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label ="Mapa de Calor Comercial", menu=menu_principal)

    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label ="Alertas y Notificaciones", menu=menu_principal)
    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label ="Disponibilidad del Producto", menu=submenu)

    submenu.add_command(label = 'Disponibilidad Total del Producto')
    submenu.add_command(label = 'Falta de Stock')

    menu_acerca_de = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Acerca de", menu=menu_acerca_de)
    menu_acerca_de.add_command(label="Del proyecto", command=mostrar_info_proyecto)
    menu_acerca_de.add_command(label="De esta APP", command=mostrar_info_app)

    menu_principal = tk.Menu(barra_menu)
    barra_menu.add_cascade(label ="Ayuda", menu=menu_principal)
    submenu = tk.Menu(menu_principal)
    menu_principal.add_cascade(label ="Solicitud de ayuda", menu=submenu)

    submenu.add_command(label = 'Cliente Nuevo')
    submenu.add_command(label = 'Cliente Fijo')
    submenu.add_command(label = "Numero de CUIT del cliente nuevo")

    submenu.add_command(label = 'Alta de Productos')
    submenu.add_command(label = 'Baja de Productos')

    boton1.pack(side="left")
    boton2.pack(side="left")
    boton3.pack(side="left")
    boton4.pack(side="left")
    boton5.pack(side="left")
    boton6.pack(side="left")
    # Bloqueo de ventana hija 
    ventana.transient()
    ventana.grab_set()
    ventana.wait_window()
    ventana.mainloop()
#Ya no se usa mainloop()
#ventana.mainloop()