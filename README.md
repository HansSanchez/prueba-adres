# Prueba Técnica para Full Stack
Esta aplicación Django es un proyecto Full Stack desarrollado como parte de una prueba técnica. Incluye una interfaz de usuario frontend para gestionar adquisiciones, así como una API backend robusta para soportar estas funcionalidades. La aplicación permite a los usuarios crear, consultar, modificar, desactivar adquisiciones y visualizar su historial.

## Prerequisitos
Antes de comenzar, asegúrate de tener instalado:

- Python (versión 3.x)
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado para crear entornos virtuales)

## Instalación
Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

### Clonar el Repositorio
Primero, clona el repositorio de Git a tu máquina local utilizando el siguiente comando:

### bash
git clone https://github.com/HansSanchez/prueba-adres.git

### Crear y Activar un Entorno Virtual (Opcional)
Es recomendable utilizar un entorno virtual para mantener las dependencias del proyecto separadas y organizadas. Para crear y activar un entorno virtual, ejecuta:

virtualenv venv

### En Windows
venv\Scripts\activate

### En Unix o MacOS
source venv/bin/activate

### Instalar Dependencias
Instala todas las dependencias requeridas para el proyecto ejecutando:

pip install -r requirements.txt

### Configuración de la Base de Datos
Configura tu base de datos según las necesidades de tu proyecto.

### Migraciones Iniciales
Antes de ejecutar el servidor, realiza las migraciones iniciales con:

python manage.py makemigrations
python manage.py migrate

### Crear un Superusuario (Opcional)
Para acceder al panel de administración de Django, crea un superusuario:

python manage.py createsuperuser

### Ejecutar el Servidor de Desarrollo
Finalmente, inicia el servidor de desarrollo con:

python manage.py runserver


