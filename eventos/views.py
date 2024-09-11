from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

def LogoutView(request):
    logout(request)
    success_url = "/eventos/"
    return redirect(success_url)

class ListarEventos(ListView):
    model = Evento
    template_name = "listarEventos.html"

class CrearEvento(CreateView):
    model = Evento
    template_name = "crearEvento.html"
    form_class = EventoForm
    success_url = "/eventos/"

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class EditarEvento(UpdateView):
    model = Evento
    template_name = "editarEvento.html"
    form_class = EventoForm
    success_url = "/eventos/"

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id = self.kwargs.get('id')
        return Evento.objects.get(id=id)

@login_required(login_url="/login/")
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

    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class EditarOrganizador(UpdateView):
    model = Organizador
    template_name = "editarOrganizador.html"
    form_class = OrganizadorForm
    success_url = "/organizadores/"
    @method_decorator(login_required(login_url="/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_object(self):
        id = self.kwargs.get('id')
        return Organizador.objects.get(id=id)

@login_required(login_url="/login/")
def EliminarOrganizador(request, id):
    organizador = Organizador.objects.get(id=id)
    organizador.delete()
    success_url = "/organizadores/"
    return redirect(success_url)

def inicio(request):
    return render(request, "base.html")
