from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('tipo_dni', 'dni', 'nombres','tel', 'correo','url_selfi','url_documento',)