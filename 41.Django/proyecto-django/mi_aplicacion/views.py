from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse


def categoria_lista(request):
    categoria = models.Categoria.objects.all()
    contexto = {'categotia': categoria}
    return render(request, 'lista_categoria.html', contexto)


def detalle_categoria(request, pk):
    categoria = get_object_or_404(models.Categoria, pk=pk)
    contexto = {'categoria': categoria}
    return render(request, 'detalle_categoria.html', contexto)
