import django.forms as forms
from django.forms.widgets import DateInput
from .models import Evento, Organizador


class EventoForm(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = Evento
        fields = ["nombre", "fecha", "organizador"]

    def clean_nombre(self):
        nombre = self.data.get('nombre')
        if self.data.get('nombre').lower() == "cancelado":
            raise forms.ValidationError("El nombre no puede ser Cancelado")
        return nombre


class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ["nombre", "email"]
