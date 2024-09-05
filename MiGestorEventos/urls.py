from django.contrib import admin
from django.urls import path

# ruta para eventos para crear para eliminar y editar y tambien ruta para organizadores y para crear
urlpatterns = [
    path("eventos/", None),
    path("eventos/crear/", None),
    path("eventos/eliminar/", None),
    path("eventos/editar/", None),
    path("organizadores/", None),
    path("organizadores/crear/", None),
    path("admin/", admin.site.urls),
]
