from django.db import models

# Create your models here.
class Productos (models.Model):
    opciones = (
        ("Café", "C"),
        ("Artículos", "A")
    )
    nombre = models.CharField(max_length=60)
    precio = models.FloatField()
    costo = models.FloatField()
    foto = models.ImageField(blank = True, null=True)
    categoria = models.CharField(choices=opciones, max_length=20, blank= True, null=True)  #chocices => tener una estructura que contenga diferentes opciones
    cod_barras = models.CharField(primary_key=True, max_length=100)

    def cambiarPrecio (self,nuevoprecio):
        self.precio = nuevoprecio

    def cambiarCosto (self,nuevocosto):
        self.costo = nuevocosto

    def cambiarNombre (self,nuevonombre):
        self.nombre = nuevonombre

    def cambiarFoto (self,nuevafoto):
        self.foto = nuevafoto

    def __str__(self):
        #Brindar una identificación general en base de datos (sección 'Admin')
        return self.nombre