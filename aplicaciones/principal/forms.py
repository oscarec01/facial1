from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
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
        widgets = {
            'tipo_dni': forms.Select(
                attrs={
                    'class': 'form-control border'
                }
            ),
            'dni': forms.NumberInput(
                attrs={
                    'class': 'form-control border'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control border'
                }
            ),
            'tel': forms.NumberInput(
                attrs={
                    'class': 'form-control border'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control border'
                }
            ),
            'url_selfi': forms.FileInput(
                attrs={
                    'class': 'form-control-file border'
                }
            ),
            'url_documento': forms.FileInput(
                attrs={
                    'class': 'form-control-file border'
                }
            ),
        }
