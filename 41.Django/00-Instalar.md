## Introccion e instalacion de Django

Para utilizar Django, primero necesitamos instalar el programa desde la página oficial de Django: https://www.djangoproject.com.

1. Navega a la pestaña de descargas.
2. Selecciona la opción de descarga adecuada para tu sistema operativo.

## Creación y activación del entorno virtual

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
python -m venv env
```

Este comando creará un directorio llamado env_django que contendrá el entorno virtual.

5. Ahora hay que activar el entorno ejecutando el siguiente comando:

```bash
# para mac o linux
source env_django/bin/activate
```

**Nota:** Asegúrate de estar en la misma ubicación donde creaste tu entorno virtual antes de ejecutar este comando.

```bash
# para windows
source ./venv/bin/activate
```

la terminal cambiara el promt a (env), indica que se esta trabajando dentro de un entorno virtual.

## Instalación de Django

6. Ahora si instalamos Django

```bash
# en el momento de mis apuntes este era la version
py -m pip install Django==5.0.6
```

o tambien dentro del directorio proyecto crear un archivo requirements.txt con django dentro

```bash
Django
```

y luego ejecutas el siguiente comando

```bash
pip install -r requerimientos.txt
```

Con este comando, el marco de Django comenzará a descargarse. Una vez finalizada la descarga, podemos empezar a desarrollar la aplicación.

## Creación de un proyecto con django-admin

7. Crea un nuevo proyecto Django: Utiliza el comando:
   django-admin startproject <nombre_del_proyecto>
   para crear un nuevo proyecto Django en el directorio actual.

```bash
django-admin startproject mi_tienda .
```

- Importante-. El punto final del comando es importante. Indica a django-admin que use la carpeta actual. Si deja fuera este punto final, se creará un subdirectorio adicional.

Verificamos dentro del directorio creado mi_tienda, y vemos que se ha creado un directorio con el mismo nombre y un archivo manage.py

### Exploración de la estructura del proyecto

```bash
manage.py
mi_tienda/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
```

### Archivos Principales de un Proyecto Django

- 7.0. mi_tienda: helloproject se considera como el paquete de Python para el proyecto.

- 7.1. init.py: es un archivo vacío que funciona para indicar a Python que este directorio se debe considerar como un paquete.

- 7.2. settings.py: Aquí se configuran las opciones y ajustes específicos para tu proyecto Django, como la base de datos, las aplicaciones instaladas, la configuración del servidor de correo electrónico, entre otros.

- 7.3. urls.py: Define todas las URL de tu proyecto y mapea las URL a las vistas correspondientes que manejan las solicitudes HTTP entrantes.

- 7.4. asgi.py y wsgi.py sirven como punto de entrada para los servidores web en función del tipo de servidor implementado.

- 7.5. manage.py: Una utilidad de línea de comandos que te permite ejecutar varios comandos para administrar tu proyecto Django, como iniciar el servidor de desarrollo, crear y aplicar migraciones de base de datos, crear un superusuario y ejecutar pruebas.

8. Ejecutamos el servidor de desarrollo de Django con el siguiente comando:

NOTA: verifica que estas dentro de el directorio my_store

```bash
python manage.py runserver
```

9. Creamos un archivo dentro de mi_tienda/views.py, esto mas por temas de convencion

con este ultimo paso creamos un proyecto de django

## Creación de la aplicación mi_aplicacion

Hemos descubierto los aspectos básicos sobre el marco de Django y examinado la estructura de carpetas de nuestro proyecto. Ahora es el momento de crear nuestra primera aplicación. La aplicación ¡mi_aplicacion! permitirá comprender cómo se crean las aplicaciones y cómo funcionan al unísono con el proyecto de Django.

dentro del mismo directorio de my_store ejecutar el siguiente comando:

```bash
python manage.py startapp mi_aplicacion
```

Con este comando, Django crea las carpetas y los archivos necesarios, y la estructura siguiente ahora debería estar visible.

```bash
mi_aplicacion/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Registro de la aplicación en el proyecto

Dado que las aplicaciones y los proyectos son independientes en Django, debe registrar la aplicación en el proyecto.

1. Dentro de my_store, abra settings.py.

2. Busque la lista INSTALLED_APPS, que debe estar en la línea 33.

3. Agregue lo siguiente al final de la lista, entre corchetes ([ ]):

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_aplicacion.apps.MiAplicacionConfig', # agregar linea
]
```
