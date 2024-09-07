from django.contrib import admin
from django.urls import path
from eventos.views import (
    CrearEvento,
    CrearOrganizador,
    ListarEventos,
    ListarOrganizadores,
    blanco,
)

urlpatterns = [
    path("eventos/", ListarEventos.as_view(), name="eventos"),
    path("eventos/crear/", CrearEvento.as_view(), name="crearEvento"),
    path("eventos/eliminar/", blanco),
    path("eventos/editar/", blanco),
    path("organizadores/", ListarOrganizadores.as_view(), name="organizadores"),
    path("organizadores/crear/", CrearOrganizador.as_view(), name="crearOrganizador"),
    path("admin/", admin.site.urls),
]
