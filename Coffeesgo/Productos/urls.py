# especificamos las direcciones de las Apis

from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from Productos.views import CategoriaAPI, ProductoAPI, ComentarioAPI



router = DefaultRouter()
router.register('categoria', CategoriaAPI)
router.register('producto', ProductoAPI)
router.register('comentario', ComentarioAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]