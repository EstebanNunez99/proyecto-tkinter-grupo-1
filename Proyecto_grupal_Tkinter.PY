import tkinter as tk

def Trabajo():
    print()


ventana = tk.Tk()
ventana.title ("Trabajo Grupo 1")
ventana.geometry ("500x400")

etiqueta = tk.Label(ventana, text="Panel de Ventas", font=("Elephant", 25))
etiqueta.pack()

boton1 = tk.Button(ventana, text="Fecha", font=("Arial Black", 12), command= Trabajo)
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

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label ="Tasa de Conversion", menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label ="Tasa Fija en Pesos o en Dólares", menu=submenu)

submenu.add_command(label = 'Pesos')
submenu.add_command(label = 'Dolares (Cotizacion actual en Linea)')

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

ventana.mainloop()
