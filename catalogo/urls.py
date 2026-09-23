from django.urls import path
from .views import vista_detalle, vista_productos, vista_contacto

urlpatterns = [
    path('detalle', vista_detalle, name='detalle'),
    path('productos/', vista_productos, name='productos'),
    path('contacto/', vista_contacto, name='contacto'),
]