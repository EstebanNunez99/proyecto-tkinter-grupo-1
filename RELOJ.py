import tkinter as tk 
import time
#Cambio: no crea una ventana principal, ahora solo es un widget
# ventana = tk.Tk() 
# ventana.title ('Reloj simple')
# ventana.geometry('600x300')

#Cambio: Envyuelvo todo en una funcion que recibe como parametro a un frame
def crear_reloj(frame_padre):    
    reloj = tk.Label( frame_padre, font= ('Broadway', 60), bg = 'pink', fg= 'black')

    def hora():
        tiempo_actual = time.strftime ('%H:%M:%S')
        reloj.config(text = tiempo_actual)
        reloj.after (1000, hora)
        reloj.pack(anchor = 'center')  
    hora() 
#CAmbio: ahora ya no es ventana principal, no ejecura mainloop
# ventana.mainloop()