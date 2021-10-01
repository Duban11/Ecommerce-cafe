#serializador => herramienta que permite que convertir objetos en diccionarios
from django.db.models import fields
from rest_framework import serializers
from Productos.models import *

class CategoriaSerial(serializers.ModelSerializer):
    class Meta:
        #MetaClasefunciona  => flexibiliza la forma en como funciona una clase
        model = CategoriaProducto
        fields = ['nombre', 'imagen', 'numeroProductos']


class ProductoSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'imagen', 'calificacion','calcularCalificacion']


class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'