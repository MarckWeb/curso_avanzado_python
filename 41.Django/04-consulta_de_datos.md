## Configuración del shell interactivo

Django incluye un shell interactivo en el que puede ejecutar código de Python en el entorno de Django.

- el comando siguiente para iniciar el shell:

```bash
python manage.py shell
```

- Importe los modelos desde models dentro de mi_aplicacion:

```bash
from mi_aplicacion.models import Categoria, Producto
```

## Creación y modificación de objetos

Dado que los modelos son clases de Python, las nuevas instancias se crean con la misma sintaxis que usaríamos para crear un objeto. Dado que heredan de Django.models.Model, heredan la funcionalidad del ORM de Django. Esa funcionalidad incluye save, que se usa para guardar el objeto en la base de datos.

1. Creamos una nueva categoria

```python
categoria = Categoria(nombre="Ordenadores", descripcion="categoria ordenadores")
categoria.save()
```

La parte save escribirá el objeto en la base de datos. Como lo hemos creado desde cero, ejecutará una instrucción INSERT en la base de datos.

2. Actualice la categoria a tipos de ordenadores; para ello, establecemos el campo descripcion llamando a save:

```python
categoria.descripcion="tipos de ordenadores"
categoria.save()
```

3. Cree dos nuevos productos para la categoria ejecutando los comandos de Python siguientes en el Shell:

```python
Producto(nombre="Laptop Acer", descripcion="Laptop potente y confiable para trabajo", precio=799.99, stock=10, categoria=categoria).save()
Producto(nombre="Laptop Dell", descripcion="Laptop versátil", precio=899.99, stock=5, categoria=categoria).save()
```
