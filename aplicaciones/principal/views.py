from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Usuarios, Tiposdni, Estado
from .forms import UsuarioForm, PersonaForm

def inicio(request):
    return render(request, 'index.html')

# Usuarios
def nuevo_usuario(request):
    if request.method == "POST":
        formaUsuario = UsuarioForm(request.POST)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('index')
    else:
        formaUsuario = UsuarioForm()
    return render(request, 'nuevo_usuario.html', {'formaUsuario': formaUsuario})


def editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if request.method == 'POST':
        formaUsuario = UsuarioForm(request.POST, instance=usuario)
        if formaUsuario.is_valid():
            formaUsuario.save()
            return redirect('index')
    else:
        formaUsuario = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'formaUsuario': formaUsuario})


def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto={
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        form = PersonaForm()
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
            
    return render(request, 'crear_persona.html',contexto)