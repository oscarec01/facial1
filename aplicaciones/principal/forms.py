from django.forms import ModelForm, EmailInput, PasswordInput
from .models import Usuarios

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
