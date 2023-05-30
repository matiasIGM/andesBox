# andesBox

Descripción breve

## Instalación

1. Clona este repositorio en tu máquina local.

2. Crea un entorno virtual para el proyecto:
python -m venv env

3. Activa el entorno virtual:
- En Windows:
  ```
  .\env\Scripts\activate
  ```
- En sistemas basados en Unix (Linux, macOS):
  ```
  source env/bin/activate
  ```

4. Instala las dependencias requeridas con el siguente comando:
5. 
pip install -r requirements.txt

## Uso

1. Navega al directorio raíz del proyecto:
cd ruta/al/proyecto

2. Ejecuta las migraciones para configurar la base de datos:

python manage.py makemigrations
python manage.py migrate

Estos comandos crearán y aplicarán las migraciones necesarias para tu base de datos.

3. Inicia el servidor de desarrollo:

python manage.py runserver

Ahora puedes acceder a la aplicación en http://localhost:8000

