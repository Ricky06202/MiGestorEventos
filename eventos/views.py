from django.http import HttpResponse
from django.shortcuts import render
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm
from django.views.generic import ListView, CreateView


class ListarEventos(ListView):
    model = Evento
    template_name = "listarEventos.html"


class CrearEvento(CreateView):
    model = Evento
    template_name = "crearEvento.html"
    form_class = EventoForm
    success_url = "/eventos/"


class ListarOrganizadores(ListView):
    model = Organizador
    template_name = "listarOrganizadores.html"


class CrearOrganizador(CreateView):
    model = Organizador
    template_name = "crearOrganizador.html"
    form_class = OrganizadorForm
    success_url = "/organizadores/"


def blanco(request):
    return HttpResponse(b"Hola, Mundo!")
