from django.shortcuts import render, redirect
from .models import Persona, Usuarios, Tiposdni, Estado
from .forms import PersonaForm

def inicio(request):
    return render(request, 'index.html')

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
        form.save()
        return redirect('index')
        
    
    return render(request, 'crear_persona.html',contexto)
