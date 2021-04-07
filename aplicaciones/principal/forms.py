from django.forms import ModelForm, EmailInput, PasswordInput
from .models import Usuarios, Persona

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = (
            'tipo_dni',
            'dni',
            'nombres',
            'usuario',
            'contrasenia'
        )
        widtgets = {
            'contrasenia': PasswordInput(attrs={'type': 'password'})
        }


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = (
            'tipo_dni',
            'dni',
            'nombres',
            'tel', 
            'correo',
            'url_selfi',
            'url_documento',
        )