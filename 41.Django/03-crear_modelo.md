# Crear modelos en Django

El primer paso para desarrollar una aplicación en Django es definir los modelos, que representan la estructura de datos de la aplicación. Los modelos se definen en un archivo llamado `models.py` dentro de cada aplicación de Django.

### Ejemplo de modelos de refugio de perros:

En el archivo `models.py`, definimos dos clases de Python para representar nuestros modelos:

```python
# Create your models here
class Refugio(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Perro(models.Model):
    refugio = models.ForeignKey(Refugio, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
```

Aquí, Refugio representa un lugar donde se alojan los perros, y Perro representa un perro en particular. Observe la relación entre Perro y Refugio: un refugio puede tener muchos perros, pero un perro solo puede estar en un refugio a la vez.

## Registro del modelo:

Después de definir los modelos, debemos registrar la aplicación en el archivo settings.py del proyecto para que Django la reconozca. Esto se hace agregando el nombre de la aplicación al INSTALLED_APPS.

```py
# settings.py
INSTALLED_APPS = [
    'dog_shelters.apps.DogSheltersConfig',
    'dog_shelters.apps.DogSheltersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Al agregar la aplicación a INSTALLED_APPS, Django sabe que debe incluir esta aplicación al ejecutar el proyecto.
