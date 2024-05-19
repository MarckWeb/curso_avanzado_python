## Crear la vista

Dentro de del proyecto, abra views.py, que estará dentro de mi_aplicacion.

Reemplace el código que hay dentro de views.py por el siguiente:

```py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mi primer proyecto con django!")
```

La función auxiliar HttpResponse permite devolver texto u otros tipos primitivos al autor de la llamada.

## Creación de la ruta

Dentro de mi_tienda, hay un archivo denominado urls.py. y agrega el siguiente codigo que falta

```py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
```

La parte más importante de este código es la tupla urlpatterns. Esta tupla es donde las vistas y las direcciones URL están conectadas o asignadas. Tal como se puede ver, hemos importado nuestro archivo views.py para poder usarlo en la línea urlpatterns.

## Registro de nuestro elemento URLconf con el proyecto

Nuestro elemento URLconf recientemente creado está dentro de nuestra aplicación mi_aplicacion. Dado que el proyecto controla todas las solicitudes de los usuarios, es necesario registrar nuestro elemento URLconf en el archivo principal urls.py, que está dentro de mi_tienda.

- Reemplazamos la línea que lee _from django.urls import path_ con la instrucción import siguiente para agregar include y path.

```py
from django.urls import include, path
```

El uso de include nos permite importar módulos de URLconf, y path se usa para identificar la raíz de URLconf.

- Dentro de la lista, debajo de la línea que lee urlpatterns = [, agregue el código siguiente:

```py
path('', include('mi_tienda.urls')),
```

1. Crear la vista: En tu archivo views.py, que estará dentro de la . aplicación "mi_aplicacion", defines una función llamada index que toma un argumento request y devuelve una respuesta de tipo HttpResponse con el texto "Hello, world!".

```py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo!")
```

2. Creación de la ruta: Luego, en un nuevo archivo llamado urls.py dentro de la aplicación "mi_aplicacion", defines las rutas para tu aplicación. En este caso, solo hay una ruta definida que coincide con la URL raíz (''), y se asigna a la vista index que acabas de definir.

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

3. Registro de nuestro elemento URLconf con el proyecto: Ahora, debes registrar las URL de tu aplicación con el proyecto principal mi_tienda. Para hacer esto, en el archivo urls.py del proyecto principal (mi_tienda), importas include y agregas la ruta de tu aplicación usando include('mi_aplicacion.urls').

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('mi_aplicacion.urls')),
    path('admin/', admin.site.urls),
]
```

4. Ejecución de la primera aplicación: Finalmente, ejecutas el servidor de desarrollo de Django con el comando python manage.py runserver en la terminal. Esto hace que tu aplicación esté disponible en http://localhost:8000/, donde podrás ver el mensaje "Hello, world!".
