# Proyecto de Python con la libreria tkinter
## Punto de Venta - Proyecto Grupo 1
## Integrantes
    - Esteban
    - Lorena
    - Juan
    - Ricardo

## Descripción
    Este proyecto tiene como objetivo desarrollar un sistema de escritorio básico para la
    gestión de ventas de un kiosco, usando como lenguaje de programación Python e integrando una
    interfaz gráfica con la libreria Tkinter. Este proyecto fue creado como trabajo práctico de
    la Etapa 2 del Informatorio

### Características Principales
    Una lista de lo que hace el software. //Tdv incompleto
    - Registro de ventas en tiempo real.

    - Conexión a base de datos MySQL.

    - Cálculo de total de la venta.

    - Reloj integrado en la interfaz.

    - Historial de ventas (Futuro).

    - Gestión de inventario (Futuro).

### Stack Tecnológico 

    - Lenguaje: Python

    - Interfaz Gráfica (GUI): Tkinter

    - Base de Datos: MySQL

    - Conector Python-MySQL: mysql-connector-python

### Estructura de la Base de Datos (Schema)
El sistema utiliza una base de datos MySQL (`kiosco_db`) con tres tablas relacionales para asegurar la integridad de los datos.

### Tabla: `Productos`
Almacena el inventario físico del kiosco.
* `id_producto` (INT, PK): Identificador único del producto.
* `nombre` (VARCHAR): Nombre del producto.
* `precio` (DECIMAL): Precio de venta unitario.
* `stock` (INT): Cantidad disponible en inventario.

### Tabla: `Ventas`
Almacena un registro (ticket) por cada transacción completada.
* `id_venta` (INT, PK): Identificador único de la venta.
* `fecha_hora` (DATETIME): Marca de tiempo de cuándo se realizó la venta.
* `total_venta` (DECIMAL): Suma total de la transacción.

### Tabla: `Detalle_Ventas`
Actúa como tabla pivote, conectando `Ventas` y `Productos`. Almacena cada línea de item de una venta.
* `id_detalle` (INT, PK): Identificador único del detalle.
* `id_venta` (FK): Referencia a la tabla `Ventas`.
* `id_producto` (FK): Referencia a la tabla `Productos`.
* `cantidad` (INT): Cuántas unidades de este producto se vendieron.
* `precio_en_venta` (DECIMAL): El precio del producto al momento de la venta (para guardar el historial de precios).

### Requisitos e Instalación
    Pasos básicos: //falta completar
1.  **Clonar el Repositorio**
    ```bash
    git clone (https://github.com/EstebanNunez99/proyecto-tkinter-grupo-1.git)
    cd (proyecto-tkinter-grupo-1)
    ```
2.  **Crear y Activar un Entorno Virtual**
    ```bash
    python3 -m venv venv
    
    Comando para entrar al entorno virtual
    source venv/bin/activate

    Comando para salir del entorno virtual
    deactivate
    ```

3.  **Instalar Librerías**
(Dentro del entorno virtual)
    ```bash
    pip install mysql-connector-python python-dotenv
    ```

4.  **Configurar Variables de Entorno**
    Crea un archivo llamado `.env` en la raíz del proyecto. Copiar formato del archivo `.env.example` 
    *Cambiar los valores por tus datos originales*

5.  **Ejecutar la aplicación**
    python3 main.py
