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

Tener en cuenta que no hemos configurado una variable local para cada instancia Producto. Dado que no se reutilizarán los objetos, no es necesario establecerlos en una variable.

## Recuperación de objetos

recuperar todos los productos

```python
categoria.producto_set.all()
```

salida

```bash
<QuerySet [<Producto: Laptop Acer>, <Producto: Laptop Dell>]>
```

La función get devolverá solo un objeto. Puede pasar parámetros a get para proporcionar una cadena de consulta. Aquí usamos pk, que es una palabra clave especial para indicar la clave principal. El resultado devuelto será:

```python
<Producto: Laptop Acer>
```

Recupere todos los perros del refugio de demostración mediante filter tal como se muestra en el comando siguiente:

```python
productos_teclado = Producto.objects.filter(categoria__nombre='Teclado')
```

Al igual que get, filter nos permite pasar una consulta en los parámetros. Observe que podemos usar dos caracteres de subrayado para ir de propiedad en propiedad. Dado que queremos encontrar todos los productos de la categoria denominado teclado, usamos categorianombre para acceder a la propiedad nombre categoria. El resultado devuelto será todos los ordenadores, porque solo tenemos una categoria.
