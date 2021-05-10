from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import (
    LoginView,
)
from django.contrib.auth import logout
from .models import Persona, Tiposdni, Estado
from .forms import PersonaForm


def inicio(request):
    return render(request, 'index.html')


def prueba(request):
    return render(request, 'prueba.html')


def header(request):
    return render(request, 'include/header.html')


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
