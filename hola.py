from tkinter import *
from tkinter import ttk

# Este archivo fue creado tomando como referencia la documentacion oficial de Tkinter
#https://docs.python.org/3/library/tkinter.html
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Bienvenidos, somos el grupo 1').grid(column=0, row=0)
ttk.Label(frm, text='-----------------------------').grid(column=0, row=1)#Todavia no se como agregar una linea separadora
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=2)
root.mainloop()