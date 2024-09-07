import django.forms as forms
from django.forms.widgets import DateInput
from .models import Evento, Organizador


class EventoForm(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = Evento
        fields = ["nombre", "fecha", "organizador"]

    def validarNombre(self):
        if self.cleaned_data["nombre"] == "Cancelado":
            raise forms.ValidationError("El nombre no puede ser Cancelado")


class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ["nombre", "email"]
