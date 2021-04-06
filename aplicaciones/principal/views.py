from django.shortcuts import render
from .models import Persona, Usuarios, Tiposdni, Estado

def inicio(request):
    return render(request, 'index.html')
