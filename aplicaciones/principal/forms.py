from django.forms import ModelForm, EmailInput, PasswordInput, TextInput, Select, NumberInput, ChoiceField
from django import forms
from .models import Usuarios, Persona, Usuario


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
            'tipo_dni': Select(attrs={"class": "form-control"}),
            'dni': NumberInput(attrs={"class": "form-control"}),
            'nombres': TextInput(attrs={"class": "form-control"}),
            'usuario': EmailInput(attrs={"class": "form-control"}),
            'contrasenia': PasswordInput(attrs={"class": "form-control", "type": "password"})
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


class FormUser(ModelForm):
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password...',
            'id': 'password1',
            'required': 'required'
        }
    ))

    password_2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter again your password...',
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'name',
            'lastname'
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Email',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Name',
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Lastname',
            })
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden !!!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
