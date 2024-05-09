from django.contrib import admin
from django.urls import path

# Importación de las vistas definidas en el archivo 'views.py'
from . import views

# se indica al servidor cómo manejar las solicitudes HTTP para una URL particular, es decir, qué vista debe mostrarse cuando alguien accede a esa URL en tu sitio web.
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
