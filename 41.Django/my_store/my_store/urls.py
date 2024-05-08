from django.contrib import admin
from django.urls import path

# Importación de las vistas definidas en el archivo 'views.py'
from . import views

urlpatterns = [
    # aqui se conecta las vistas y las urls
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
