from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Usuarios, Tiposdni, Estado
from .forms import UsuarioForm

def inicio(request):
    return render(request, 'index.html')

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

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, pk=id)
    if usuario:
        usuario.delete()
    return redirect('usuarios')
