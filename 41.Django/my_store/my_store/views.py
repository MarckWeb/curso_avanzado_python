from django.shortcuts import render
from django.http import HttpResponse

# Esta vista toma un objeto 'request' como argumento y devuelve una respuesta HTTP


def index(request):
    return render(request, 'index.html', {
        # dentro de las variables podemos pasar cualquier dato
        'message': 'Listado de productos',
        'title': 'Tienda',
        'products': [
            {'title': 'Pantalla', 'price': 150.25, 'stock': True},
            {'title': 'Mouse', 'price': 5, 'stock': True},
            {'title': 'Teclado', 'price': 12.25, 'stock': False},
            {'title': 'Camara', 'price': 25, 'stock': True}
        ]
    })
