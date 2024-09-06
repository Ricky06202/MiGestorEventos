from django.http import HttpResponse
from django.shortcuts import render
from .models import Evento


# crea una vista para los eventos pero basa en clases
class EventosView:
    def get(self, request):
        eventos = Evento.objects.all()
        return render(request, "eventos.html", {"eventos": eventos})
def blanco(request):
    return HttpResponse("Hola, Mundo!")
