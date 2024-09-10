from django.contrib import admin
from django.urls import path
from eventos.views import (
    CrearEvento,
    CrearOrganizador,
    ListarEventos,
    ListarOrganizadores,
    inicio,
    EditarEvento,
    EliminarEvento,
    EliminarOrganizador,
    EditarOrganizador,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("eventos/", ListarEventos.as_view(), name="eventos"),
    path("eventos/crear/", CrearEvento.as_view(), name="crearEvento"),
    path("eventos/eliminar/<id>/", EliminarEvento, name="eliminarEvento"),
    path("eventos/editar/<id>/", EditarEvento.as_view(), name="editarEvento"),
    path("organizadores/", ListarOrganizadores.as_view(), name="organizadores"),
    path("organizadores/crear/", CrearOrganizador.as_view(), name="crearOrganizador"),
    path("organizadores/editar/<id>", EditarOrganizador.as_view(), name="editarOrganizador"),
    path("organizadores/eliminar/<id>", EliminarOrganizador, name="eliminarOrganizador"),
    path("admin/", admin.site.urls),
]
