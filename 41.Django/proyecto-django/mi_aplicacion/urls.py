from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_lista, name='lista_categoria'),
    path('categoria/<int:pk>', views.detalle_categoria, name='detalle_categoria')
]
