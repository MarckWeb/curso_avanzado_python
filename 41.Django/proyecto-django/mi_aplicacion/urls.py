from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_lista, name='categoria_lista'),
    path('categoria/<int:pk>', views.detalle_categoria, name='categoria_detalle')
]
