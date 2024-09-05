import django.forms as forms
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["nombre", "fecha", "organizador"]

    def validarNombre(self):
        if self.cleaned_data["nombre"] == "Cancelado":
            raise forms.ValidationError("El nombre no puede ser Cancelado")
