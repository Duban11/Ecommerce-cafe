from rest_framework import viewsets

from Productos.models import *
from Productos.serializers import *

class CategoriaAPI(viewsets.ModelViewSet):
    serializer_class = CategoriaSerial
    #queryset = > especificamos los objetos que queremoos comunicar con el frontend
    queryset = CategoriaProducto.objects.all()

class ProductoAPI(viewsets.ModelViewSet):
    serializer_class = ProductoSerial
    queryset = Producto.objects.all()


class ComentarioAPI(viewsets.ModelViewSet):
    serializer_class = ComentarioSerial
    queryset = Comentario.objects.all()
     
