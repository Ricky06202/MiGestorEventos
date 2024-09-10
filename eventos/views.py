from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm
from django.views.generic import ListView, CreateView, UpdateView


class ListarEventos(ListView):
    model = Evento
    template_name = "listarEventos.html"


class CrearEvento(CreateView):
    model = Evento
    template_name = "crearEvento.html"
    form_class = EventoForm
    success_url = "/eventos/"

class EditarEvento(UpdateView):
    model = Evento
    template_name = "editarEvento.html"
    form_class = EventoForm
    success_url = "/eventos/"

    def get_object(self):
        id = self.kwargs.get('id')
        return Evento.objects.get(id=id)

def EliminarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    success_url = "/eventos/"
    return redirect(success_url)

class ListarOrganizadores(ListView):
    model = Organizador
    template_name = "listarOrganizadores.html"


class CrearOrganizador(CreateView):
    model = Organizador
    template_name = "crearOrganizador.html"
    form_class = OrganizadorForm
    success_url = "/organizadores/"

class EditarOrganizador(UpdateView):
    model = Organizador
    template_name = "editarOrganizador.html"
    form_class = OrganizadorForm
    success_url = "/organizadores/"

    def get_object(self):
        id = self.kwargs.get('id')
        return Organizador.objects.get(id=id)

def EliminarOrganizador(request, id):
    organizador = Organizador.objects.get(id=id)
    organizador.delete()
    success_url = "/organizadores/"
    return redirect(success_url)

def inicio(request):
    return render(request, "base.html")
