# Crear modelos en Django

El primer paso para desarrollar una aplicación en Django es definir los modelos, que representan la estructura de datos de la aplicación. Los modelos se definen en un archivo llamado `models.py` dentro de cada aplicación de Django.

### Ejemplo de modelos de mi_tienda:

En el archivo `models.py` de mi aplicacion, definimos dos clases de Python para representar nuestros modelos:

```python
# Crear los modelos

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
```

Aquí, categoria representa donde pertenece el producto, y Producto representa al producto. Observe la relación entre Categoria y producto: una categori puede tener muchos productos, pero un producto solo puede estar en una categoria a la vez.

## Registro del modelo:

Después de definir los modelos, debemos registrar la aplicación en el archivo settings.py del proyecto para que Django la reconozca. Esto se hace agregando el nombre de la aplicación al INSTALLED_APPS.

1. verificamos que dentro de mi_aplicacion/apps.py la clase tenga el nombre de MiAplicacionConfig

```py
from django.apps import AppConfig


class MiAplicacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mi_aplicacion'
```

2. Abrimos setting.py de mi_tienda y agregamos la ruta

```py
# settings.py
INSTALLED_APPS = [
    'mi_aplicaccion.apps.MiAplicacionConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Al agregar la aplicación a INSTALLED_APPS, Django sabe que debe incluir esta aplicación al ejecutar el proyecto.

## Creación del esquema de base de datos

Una vez que hemos creado los modelos, podemos crear la base de datos. Usaremos el SQLite predeterminado y las herramientas disponibles en Django.

## Enumeración de todas las migraciones

introducir el comando

```bash
python manage.py showmigrations
```

la vista sera

```py
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
mi_aplicacion
 [ ] 0001_initial
sessions
 [ ] 0001_initial
```

por que se ve esto!!--Django incluye varias tablas para su sistema de administración de usuarios, la administración de sesiones y otros usos internos.

## Creación de migraciones para mi_aplicacion

Vamos a indicar a Django que se han agregado nuevos modelos y que queremos que los cambios se almacenen como una migración.

Ejecutamos el siguiente comando:

```bash
python manage.py makemigrations mi_aplicacion
```

cada que se haga cambios den los modelos se ve ejecutar el comando

## Actualizar la base de datos

El comando migrate ejecutará todas las migraciones. En el caso de SQLite, el comando también creará la base de datos si no existe. Vamos a crear la base de datos y a realizar las migraciones.

```bash
python manage.py migrate
```

vemos que se completo con un OK todos

para ver el grafico de las tablas instalar la extencion sqlite en vsc
y luego Abra la paleta de comandos seleccionando Ctrl+Mayús+P en el teclado (o Cmd+Mayús+P en un equipo Mac).

Escribir SQLite y seleccione SQLite: abrir base de datos.
