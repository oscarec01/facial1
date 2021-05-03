from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import (
    LoginView,
)
from django.contrib.auth import logout
from .models import Persona, Usuarios, Usuario
from .forms import UsuarioForm, PersonaForm, FormUser


def inicio(request):
    return render(request, 'index.html')


class CreateUser(CreateView):
    model = Usuario
    form_class = FormUser
    template_name = 'new_user.html'
    success_url = reverse_lazy('list_user')


class ListUser(ListView):
    model = Usuario
    template_name = 'list_user.html'

    def get_queryset(self):
        return self.model.objects.filter(user_active=True)


# Usuarios
def lista_usuarios(request):
    no_usuarios = Usuarios.objects.count()
    usuarios = Usuarios.objects.all()
    return render(
        request,
        'usuarios.html',
        {
            'no_usuarios': no_usuarios,
            'usuarios': usuarios
        }
    )

def prueba(request):
    return render(request, 'prueba.html')


def header(request):
    return render(request, 'include/header.html')


def login(LoginView):
    template_name = 'accounts/login.html'


def logout(request):
    logout(request)


def nuevo_usuario(request):
    if request.method == "POST":
        formaUsuario = UsuarioForm(request.POST)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('usuarios')
    else:
        formaUsuario = UsuarioForm()
    return render(request, 'nuevo_usuario.html', {'formaUsuario': formaUsuario})


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        formaUsuario = UsuarioForm(request.POST, instance=usuario)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('usuarios')
    else:
        formaUsuario = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'formaUsuario': formaUsuario})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if usuario:
        usuario.delete()
    return redirect('usuarios')


def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto={
            'form':form
        }
    else:
        form = PersonaForm(request.POST, request.FILES)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            print("Image uploaded succesfully!")
            return redirect('index')

    return render(request, 'crear_persona.html',contexto)


def consulta(request):
    no_persona = Persona.objects.count()
    persona = Persona.objects.all()
    return render(
        request,
        'consulta.html',
        {
            'no_persona': no_persona,
            'persona': persona
        }
    )


def ver_caso(request, id):
    dato = get_object_or_404(Persona, pk=id)
    dato= id
    consulta = Persona.objects.filter(id=dato)
    return render(request, 'ver_caso.html', {'consulta': consulta})
