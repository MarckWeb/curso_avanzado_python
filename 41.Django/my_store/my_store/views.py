from django.http import HttpResponse

# Esta vista toma un objeto 'request' como argumento y devuelve una respuesta HTTP


def index(request):
    # Devuelve una respuesta HTTP simple que dice 'Hola desde el archivo views.py'
    return HttpResponse('Hola desde el archivo views.py')
