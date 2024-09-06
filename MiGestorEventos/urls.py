from django.contrib import admin
from django.urls import path
from eventos.views import blanco

# ruta para eventos para crear para eliminar y editar y tambien ruta para organizadores y para crear
urlpatterns = [
    path("eventos/", blanco),
    path("eventos/crear/", blanco),
    path("eventos/eliminar/", blanco),
    path("eventos/editar/", blanco),
    path("organizadores/", blanco),
    path("organizadores/crear/", blanco),
    path("admin/", admin.site.urls),
]
