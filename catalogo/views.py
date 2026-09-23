from django.shortcuts import render
from .data import productos


def vista_detalle(request):
    contexto = {
        'producto': productos[0]
    }
    return render(request, 'detalle.html', contexto)


def vista_productos(request):
    contexto = {
        'productos': productos
    }
    return render(request, 'productos.html', contexto)


def vista_contacto(request):
    return render(request, 'contacto.html')