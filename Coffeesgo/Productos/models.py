from django.db import models
from django.db.models.deletion import CASCADE

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        #indentifar el nombre de nuestros objetos
        return self.nombre
    @property  #convierte el metodo en atributo
    def numeroProductos (self):
        productos = self.producto_set.all()
        return len(productos)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=500, blank=True, null=True )
    imagen = models.ImageField(blank=True, null=True)
    calificacion =models.FloatField(default=0)


    def __str__(self):
        return self.nombre


    @property
    def calcularCalificacion(self):
        comentarios = Comentario.objects.all()
        calificacion = 0
        for comentario in comentarios:
            calificacion += comentario.calificacion
        return calificacion/len(comentarios)
        

class Comentario(models.Model):
    usuario = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion =models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.usuario + " - " + self.producto.nombre
