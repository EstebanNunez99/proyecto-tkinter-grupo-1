# Proyecto de Python con la librería tkinter
## Punto de Venta - Proyecto Grupo 1
## Integrantes
    - Esteban
    - Lorena
    - Gisela
    - Juan
    - Ricardo

## Descripción
    Este proyecto tiene como objetivo desarrollar un sistema de escritorio básico para la
    gestión de ventas de un kiosco, usando como lenguaje de programación Python e integrando una
    interfaz gráfica con la librería Tkinter. Este proyecto fue creado como trabajo práctico de
    la Etapa 2 del Informatorio.

    El sistema unifica 4 "mini-proyectos" en una única aplicación lanzada desde un archivo `main.py` principal. Los mini-proyectos que tenemos como consigna son:
    - Barra de desplazamiento
    - Reloj
    - Agregar/Eliminar
    - Menu desplegable
    

### Características Principales
    - **Registro de Ventas:** Permite registrar productos (con nombre y precio manual) en una venta.
    - **Conexión a BD en la Nube:** Se conecta a una base de datos **PostgreSQL** hosteada en Render.
    - **Cálculo de Totales:** Calcula el subtotal por producto y el total de la venta.
    - **Reloj Integrado:** Muestra un reloj en tiempo real en la pantalla principal.
    - **Historial de Ventas:** Permite consultar un historial de las ventas guardadas en la BD.
    - **Programación Asíncrona:** Utiliza **hilos (`threading`)** para las consultas a la BD, evitando que la interfaz gráfica se congele.
    - **Panel "Acerca de":** Incluye información sobre el proyecto y las tecnologías usadas.

### Stack Tecnológico 

    - **Lenguaje:** Python 3
    - **Interfaz Gráfica (GUI):** Tkinter
    - **Base de Datos:** PostgreSQL (Hosteada en Render)
    - **Conector Python-BD:** psycopg2-binary
    - **Gestión de Entorno:** venv
    - **Variables de Entorno:** python-dotenv

### Estructura de la Base de Datos (Schema)
El sistema utiliza una base de datos PostgreSQL con dos tablas para registrar las transacciones.

#### Tabla: `Ventas`
Almacena un registro por cada transacción completada.
* `id_venta` (SERIAL, PK): Identificador único autoincremental de la venta.
* `fecha` (TIMESTAMP): Marca de tiempo (automática) de cuándo se guardó la venta.
* `total` (DECIMAL(10, 2)): Suma total de la transacción.

#### Tabla: `DetalleVenta`
Almacena cada línea de ítem correspondiente a una venta.
* `id_detalle` (SERIAL, PK): Identificador único del detalle.
* `id_venta` (FK): Referencia a la tabla `Ventas` (con `ON DELETE CASCADE`).
* `nombre_producto` (TEXT): El nombre del producto ingresado manualmente.
* `cantidad` (DECIMAL(10, 2)): Cuántas unidades se vendieron.
* `precio_unitario` (DECIMAL(10, 2)): El precio del producto al momento de la venta.

### Estructura del Proyecto
El proyecto se organiza en 5 archivos de Python principales:

* `main.py`: **(Punto de Entrada)**. Crea la ventana principal, integra el Reloj y contiene los botones para lanzar los módulos de Ventas y Panel.
* `db_connector.py`: Maneja toda la lógica de conexión a la base de datos (usando `psycopg2` y `python-dotenv`) y gestiona la ejecución de consultas en hilos separados.
* `modulo_ventas.py`: Define la sub-ventana "Nueva Venta", donde el usuario agrega productos a un carrito y guarda la venta final en la base de datos.
* `Proyecto_grupal_Tkinter.py`: Define la sub-ventana "Panel de Ventas", que contiene el botón para ver el "Historial de Ventas" y el menú "Acerca de".
* `RELOJ.py`: Módulo que provee la lógica y el widget del reloj, que es llamado por `main.py`.

### Requisitos e Instalación
    
1.  **Clonar el Repositorio**
    ```bash
    git clone [https://github.com/EstebanNunez99/proyecto-tkinter-grupo-1.git](https://github.com/EstebanNunez99/proyecto-tkinter-grupo-1.git)
    cd proyecto-tkinter-grupo-1
    ```
2.  **Crear y Activar un Entorno Virtual**
    (Recomendado para no instalar paquetes globalmente)
    ```bash
    # Crear el entorno (solo una vez)
    python3 -m venv venv
    
    # Activar el entorno (cada vez que trabajes en el proyecto)
    source venv/bin/activate
    
    # Para salir del entorno virtual
    deactivate
    ```

3.  **Instalar Librerías**
    (Dentro del entorno virtual activado)
    ```bash
    pip install psycopg2-binary python-dotenv
    ```

4.  **Configurar Variables de Entorno**
    Crea un archivo llamado `.env` en la raíz del proyecto. Debe contener la URL de conexión de Render:
    ```
    DATABASE_URL="postgresql://USUARIO:CONTRASEÑA@HOST:PUERTO/BASEDEDATOS"
    ```
    *Reemplaza la URL por tu "External Connection String" de Render.*

5.  **Crear las Tablas en la BD**
    Conéctate a tu base de datos de Render (usando `psql 'TU_URL_EXTERNA'` en tu terminal) y ejecuta el script SQL para crear las tablas `Ventas` y `DetalleVenta`.

6.  **Ejecutar la aplicación**
    (Asegúrate de tener el `venv` activado)
    ```bash
    python3 main.py
    ```