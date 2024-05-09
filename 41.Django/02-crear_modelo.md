# Desarrollo de modelos

En un proyecto web, el desarrollo de modelos es fundamental. Un modelo en Python es simplemente una clase que define la estructura de los datos que tu aplicación utilizará y cómo se almacenarán en la base de datos. En esta clase, especificas los campos o atributos que deseas tener en tu base de datos. Cada campo representa una columna en la tabla de la base de datos. Por ejemplo, podrías tener un modelo llamado 'Producto' con campos como 'nombre', 'precio' y 'descripción'. Estos modelos son esenciales para garantizar que tus datos se almacenen de manera organizada y puedan ser fácilmente accedidos y manipulados por tu aplicación.

## Creación de un modelo

los modelos son componentes fundamentales que representan la estructura y el comportamiento de los datos en una aplicación. Los modelos se definen mediante clases de Python que heredan de la clase **django.db.models.Model.** Cada atributo de la clase representa un campo de la base de datos.

```py
class Producto(models.Model):
    # detalles del modelo
    pass
```

## agregar metodos

un modelo es una clase de Python. Como resultado, puede agregar métodos e invalidar los que proporciona Django.models.Model o los que son inherentes a todos los objetos de Python.

```py
class Producto(models.Model):
    nombre = models.TextField()
# Este método se usa para mostrar un objeto si no se especifica ningún campo
    def __str__(self):
        return self.name
```

## Definición del tipo de campo

La definición del tipo de campo se refiere al tipo de dato que se almacena en un campo específico de una tabla en la base de datos. En Django, al definir modelos, especificas el tipo de campo que deseas utilizar para cada atributo, lo que determina el tipo de datos que puede contener ese campo en la base de datos

1. CharField: Un campo de texto corto que almacena cadenas de longitud limitada.

```py
nombre = models.CharField(max_length=100)
```

2. IntegerField: Un campo para almacenar números enteros.

```py
cantidad = models.IntegerField()
```

3. DateField: Un campo para almacenar fechas.

```py
fecha_publicacion = models.DateField()
```

4. BooleanField: Un campo que almacena valores booleanos (True o False).

```py
activo = models.BooleanField(default=True)
```

5. ForeignKey: Un campo que establece una relación uno a muchos con otro modelo.

```py
categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

6. ManyToManyField: Un campo que establece una relación muchos a muchos con otro modelo.

```py
etiquetas = models.ManyToManyField(Etiqueta)
```

7. DecimalField: Un campo para almacenar números decimales.

```py
precio = models.DecimalField(max_digits=10, decimal_places=2)
```

8. EmailField: Un campo para almacenar direcciones de correo electrónico.

```py
email = models.EmailField()
```

9. TextField: varias líneas de texto.
10. DateField: una fecha.
11. TimeField: una hora.
12. DateTimeField: fecha y hora.
13. URLField: una dirección URL.
14. DecimalField: un número decimal de precisión fija.

En esta sección de la documentación, encontrarás una lista completa de todos los campos de modelo disponibles en Django, junto con una descripción de cada uno y sus opciones configurables.

ejemplo de como agregar campos a la clase producto y categoria

```py
from django.db import models
class Producto(models.Model):
    nombre = models.TextField()
    precio = models.DecimalField()
    fecha_creacion = models.DateField()

class Category(models.Model):
    nombre = models.TextField()
```

## Opciones de campo

las opciones de campo se utilizan para permitir valores null o en blanco, o para marcar un campo como unico.

Las opciones de campo se pasan a la función del propio campo. Distintos campos pueden admitir distintas opciones. Algunas de las opciones más comunes son las siguientes:

- **null**: Opción booleana para permitir valores NULL. El valor predeterminado es False.

- **blank**: Opción booleana para permitir valores en blanco. El valor predeterminado es False.

- **default**: Permite la configuración de un valor predeterminado si no se proporciona un valor para el campo. Si quieres establecer el valor predeterminado en una base de datos null, establece default en None.

- **unique**: Este campo debe contener un valor único. El valor predeterminado es False.

- **min_length** y **max_length**: Se usa con tipos de cadena para identificar la longitud mínima y máxima de la cadena. El valor predeterminado es None.

- **min_value** y **max_value**: Se usa con tipos numéricos para identificar los valores mínimo y máximo.

- **auto_now** y **auto_now_add**: Se usa con tipos de fecha y hora para indicar si se debe usar la hora actual. `auto_now` siempre establecerá el campo en la hora actual al guardar, lo que resulta útil para los campos `last_update`. `auto_now_add` establecerá el campo en la hora actual en el momento de la creación, lo que resulta útil para los campos `creation_date`.

```py
# ejemplo de campos:
class Producto(models.Model):
   # Nombre del producto
    nombre = models.TextField(max_length=50, min_length=3, unique=True)
   # Precio del producto
    precio = models.DecimalField(min_value=0.99, max_value=1000)
   # Fecha de creación del producto
    fecha_creacion = models.DateField(auto_now_add=True)

class Categoria(models.Model):
   # Nombre de la categoría
    nombre = models.TextField(max_length=50, min_length=3, unique=True)  # Nombre de la categoría
```

o tambien

```py
from django.db import models
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
```

# Claves y relaciones

En las bases de datos relacionales, es común tener una clave principal para cada fila, generalmente un entero incrementado automáticamente. Django agrega automáticamente un campo id como clave principal a menos que se invalide este comportamiento.

Las relaciones entre tablas son comunes en las bases de datos relacionales. Django admite relaciones como "de uno a varios", donde varios elementos comparten un solo atributo. Para esto, se utiliza el campo ForeignKey.

Django agrega automáticamente una propiedad al objeto primario para acceder a los objetos secundarios. Por ejemplo, si un producto pertenece a una categoría, Django agregará automáticamente la propiedad product_set a la categoría para acceder a todos los productos de esa categoría.

El campo ForeignKey tiene un parámetro on_delete para indicar qué hacer cuando se elimina el objeto primario. Las opciones comunes son CASCADE, que elimina automáticamente los objetos secundarios, y PROTECT, que devuelve un error si se intenta eliminar el objeto primario con objetos secundarios relacionados.

El ForeignKey en Django debe apuntar solo a la tabla principal. Esta es la tabla que representa el objeto "padre" en la relación uno a muchos. Por ejemplo, si tienes una tabla de Producto y una tabla de Categoria, y cada producto pertenece a una categoría, entonces el campo ForeignKey debería estar en la tabla Producto y apuntar a la tabla Categoria. Esto establece la relación entre los productos y las categorías, donde cada producto está asociado con una categoría específica.

```py
from django.db import models

class Producto(models.Model):
    nombre = models.TextField()
    precio = models.DecimalField()
    fecha_creacion = models.DateField()
    categoria = models.ForeignKey(
        'Categoria',  # El nombre del modelo al que hace referencia
        on_delete=models.PROTECT  # Qué hacer si se elimina una categoría relacionada
    )

class Categoria(models.Model):
    nombre = models.TextField()  # Nombre de la categoría
    # Se creará automáticamente product_set para acceder a los productos relacionados

```

https://docs.djangoproject.com/en/5.0/ref/models/fields/
