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
