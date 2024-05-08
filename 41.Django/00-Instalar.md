## Introccion e instalacion de Django

Para utilizar Django, primero necesitamos instalar el programa desde la página oficial de Django: https://www.djangoproject.com.

1. Navega a la pestaña de descargas.
2. Selecciona la opción de descarga adecuada para tu sistema operativo.

La instalación se realiza mediante el uso de un entorno virtual. Para ello, sigue estos pasos:

1. Crea un directorio
2. Abre tu terminal.
3. Sitúate en el directorio donde deseas crear tu proyecto Django.
4. Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python3 -m venv <nombre_virtual>
```

Por ejemplo:

```bash
python3 -m venv env_django
```

Este comando creará un directorio llamado env_django que contendrá el entorno virtual.

5. Ahora hay que activar el entorno ejecutando el siguiente comando:

```bash
# para mac
source env_django/bin/activate
```

**Nota:** Asegúrate de estar en la misma ubicación donde creaste tu entorno virtual antes de ejecutar este comando.

```bash
# para windows
source env_django/scripts/activate
```

la terminal cambiara el promt a (env_django), indica que se esta trabajando dentro de un entorno virtual.

6. Ahora si instalamos Django

```bash
# en el momento de mis apuntes este era la version
py -m pip install Django==5.0.6
```

7. Crea un nuevo proyecto Django: Utiliza el comando: django-admin startproject <nombre_del_proyecto> para crear un nuevo proyecto Django en el directorio actual.

```bash
django-admin startproject my_store
```

Verificamos dentro del directorio creado my_store, y vemos que se ha creado un directorio con el mismo nombre y un archivo manage.py

### Archivos Principales de un Proyecto Django

- 7.1. **init**.py: Este archivo permite convertir al directorio creado en un módulo de Python.

- 7.2. settings.py: Aquí se configuran las opciones y ajustes específicos para tu proyecto Django, como la base de datos, las aplicaciones instaladas, la configuración del servidor de correo electrónico, entre otros.

- 7.3. urls.py: Define todas las URL de tu proyecto y mapea las URL a las vistas correspondientes que manejan las solicitudes HTTP entrantes.

- 7.4. wsgi.py: Este archivo proporciona una interfaz entre tu aplicación web Django y un servidor web, permitiendo el despliegue de tu aplicación en servidores web compatibles con WSGI.

- 7.5. manage.py: Una utilidad de línea de comandos que te permite ejecutar varios comandos para administrar tu proyecto Django, como iniciar el servidor de desarrollo, crear y aplicar migraciones de base de datos, crear un superusuario y ejecutar pruebas.

8. Ejecutamos el servidor de desarrollo de Django con el siguiente comando:

NOTA: verifica que estas dentro de el directorio my_store

```bash
python manage.py runserver
```

9. Creamos un archivo dentro de my_store/my_store views.py, esto mas por temas de convencion

ahora si empezar a codificar!!!

https://codigofacilito.com/videos/hola-mundo-fd24c295-20a2-4a9f-9bd9-b4469bc7456f
