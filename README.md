# andesBox

Descripción breve

## Instalación

1. Clona este repositorio en tu máquina local.

2. Crea un entorno virtual para el proyecto:

```
python -m venv env
```

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

```
pip install -r requirements.txt
```

## Uso

1. Navega al directorio raíz del proyecto:

```
cd ruta/al/proyecto
```
2. Ejecuta las migraciones para configurar la base de datos:

```
python manage.py makemigrations
python manage.py migrate
```
Estos comandos crearán y aplicarán las migraciones necesarias para tu base de datos.

3. Inicia el servidor de desarrollo:

```
python manage.py runserver
```
Ahora puedes acceder a la aplicación en http://localhost:8000


## Parte 2
## Documentación de la API

La documentación de la API se encuentra disponible en la siguiente ruta:

- En tu máquina local: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- En el entorno de desarrollo: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

Puedes acceder a esta URL en tu navegador para explorar la documentación interactiva de la API. Proporciona detalles sobre los endpoints disponibles, los parámetros requeridos, las respuestas esperadas y otros detalles relevantes para consumir la API correctamente.

## Realizar una petición GET a la API

Para realizar una petición GET a la API de andesBox, sigue estos pasos:

1. Abre tu herramienta o entorno de desarrollo favorito para realizar solicitudes HTTP. Puedes usar aplicaciones como cURL, Postman, Insomnia, o realizar solicitudes directamente desde tu código.

2. Asegúrate de tener la URL base de la API. En este caso, la URL base es [http://localhost:8000](http://localhost:8000) o [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. Agrega el endpoint específico para la solicitud GET que deseas realizar. Por ejemplo, si deseas obtener información sobre los envíos, el endpoint podría ser `/envios/`.

4. Incluye el API Key en la solicitud. Puedes enviarlo en los encabezados de la solicitud o como parte de los parámetros de la URL. Asegúrate de consultar la documentación de la API para conocer el formato y el nombre del encabezado o parámetro requerido para el API Key.

- **Enviar en los encabezados**: Agrega un encabezado con el nombre y el valor del API Key en tu solicitud. Por ejemplo:

  ```
  X-API-Key: tu_api_key_aqui
  ```

5. Realiza la solicitud GET a la URL completa que incluye la URL base, el endpoint y los parámetros necesarios. Recibirás la respuesta de la API con los datos solicitados.
