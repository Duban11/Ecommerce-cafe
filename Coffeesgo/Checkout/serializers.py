from rest_framework import serializers
from Checkout.models import *


class CarritoSerial (serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = ['usuario', 'fecha', 'descuento', 'cantidadMinima','total']


class InfoEnvioSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoEnvio
        fields = '__all__'   


class ArticuloSerial(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

