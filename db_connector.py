import psycopg2
import os
import threading
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    """Función simple para obtener una conexión a la BD."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def _guardar_venta_sync(lista_productos, total_venta):
    """
    usamos un hilo porque render se duerme cada 15 minutos, para evitar que se tilde la app
    """
    conn = None
    try:
        conn = get_db_connection()
        if conn is None:
            raise Exception("No se pudo conectar a la base de datos.")
        
        cur = conn.cursor()
        
        # Insertar la venta principal y obtener su ID
        sql_venta = "INSERT INTO Ventas (total) VALUES (%s) RETURNING id_venta;"
        cur.execute(sql_venta, (total_venta,))
        
        # Obtenemos el ID que la BD acaba de generar
        id_nueva_venta = cur.fetchone()[0]
        
        # Insertar cada producto en DetalleVenta
        sql_detalle = """
            INSERT INTO DetalleVenta (id_venta, nombre_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, %s);
        """
        
    
        datos_detalles = []
        for producto in lista_productos:
            nombre = producto[0]
            cantidad = producto[1]
            pu = producto[2] 
            datos_detalles.append((id_nueva_venta, nombre, cantidad, pu))
            
        cur.executemany(sql_detalle, datos_detalles)
        
        conn.commit()
        
    except Exception as e:
        print(f"Error en la transacción: {e}")
        if conn:
            conn.rollback()
        raise e 
        
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def guardar_venta_en_hilo(lista_productos, total_venta, callback_exito, callback_error):
    """
    Esta es la función que llamará Tkinter.
    Lanza la función _guardar_venta_sync en un hilo separado
    para no congelar la aplicación.
    """
    
    def trabajo_en_hilo():
        """El trabajo que hará el hilo"""
        try:
            # Llamamos a la función síncrona
            _guardar_venta_sync(lista_productos, total_venta)
            
            # Si todo sale bien, llamamos al callback de éxito
            if callback_exito:
                callback_exito()
                
        except Exception as e:
            # Si algo falla, llamamos al callback de error
            if callback_error:
                callback_error(e)

    # Creamos e iniciamos el hilo
    hilo = threading.Thread(target=trabajo_en_hilo)
    hilo.start()


def obtener_historial_ventas_sync():
    """Obtiene un resumen de todas las ventas"""
    conn = None
    try:
        conn = get_db_connection()
        if conn is None:
            raise Exception("No se pudo conectar a la base de datos.")
            
        cur = conn.cursor()
        
        sql = "SELECT id_venta, fecha, total FROM Ventas ORDER BY fecha DESC LIMIT 50;"
        cur.execute(sql)
        historial = cur.fetchall()
        return historial
        
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return [] # Retorna lista vacía en caso de error
        
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def obtener_historial_en_hilo(callback):
    """Obtiene el historial en un hilo y lo pasa a un callback"""
    
    def trabajo_en_hilo():
        historial = obtener_historial_ventas_sync()
        if callback:
            callback(historial) # El callback recibe la lista
            
    hilo = threading.Thread(target=trabajo_en_hilo)
    hilo.start()