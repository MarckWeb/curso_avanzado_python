from django.views import generic
from django.shortcuts import render, get_object_or_404
from . import models


def categoria_lista(request):
    categorias = models.Categoria.objects.all()  # Obtén todas las categorías
    # Nombre de la clave debe ser 'categorias'
    contexto = {'categorias': categorias}
    return render(request, 'lista_categoria.html', contexto)


def detalle_categoria(request, pk):
    categoria = get_object_or_404(models.Categoria, pk=pk)
    contexto = {'categoria': categoria}
    return render(request, 'detalle_categoria.html', contexto)


class detalleProductos(generic.DetailView):
    model = models.Producto
    template_name = 'producto_detalle.html'
    context_object_name = 'producto'


class CrearProducto(generic.CreateView):
    model = models.Producto
    template_name = 'producto_form.html'
    fields = ['categoria', 'nombre', 'descripcion', 'precio', 'stock']
