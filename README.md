# Proyecto de Python con la librería tkinter
## Punto de Venta - Proyecto Grupo 1
## Integrantes
    - Esteban
    - Lorena
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
    - **Empaquetador:** PyInstaller
    - **Variables de Entorno:** python-dotenv

### Cómo Usar la Aplicación

#### Opción 1: Usar el Ejecutable (Recomendado para Usuarios)

Esta es la forma más fácil de usar la aplicación sin necesidad de instalar Python.

1.  **Descargar la Carpeta:** Obtén la carpeta compilada `App-Kiosco `
2.  **Verificar Archivos:** Asegúrate de que la carpeta contenga **dos archivos** esenciales:
    * `main.exe` o `main`
    * `.env` (Este archivo es **OBLIGATORIO** y debe estar junto al ejecutable).
3.  **Ejecutar:**
    * Simplemente haz doble clic en `main.exe`.

#### Opción 2: Ejecutar desde el Código Fuente (para Desarrollo)

Esta opción es para desarrolladores que quieran modificar el código.

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/EstebanNunez99/proyecto-tkinter-grupo-1.git
    cd proyecto-tkinter-grupo-1
    ```

3.  **Instalar Librerías**
    ```bash
    pip install psycopg2-binary python-dotenv
    ```

4.  **Configurar Variables de Entorno**
    Crea un archivo `.env` en la raíz del proyecto.

5.  **Crear las Tablas en la BD**
    Conéctate a tu base de datos de Render (usando `psql 'TU_URL_EXTERNA'`) y ejecuta el script SQL para crear las tablas `Ventas` y `DetalleVenta`.

6.  **Ejecutar la aplicación**
    ```bash
    python3 main.py
    ```

### Estructura de la Base de Datos (Schema)
* **Tabla: `Ventas`** (`id_venta`, `fecha`, `total`)
* **Tabla: `DetalleVenta`** (`id_detalle`, `id_venta`, `nombre_producto`, `cantidad`, `precio_unitario`)