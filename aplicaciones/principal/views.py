from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import (
    LoginView,
)
from django.contrib.auth import logout
from .models import Persona, Tiposdni, Estado
from .forms import PersonaForm
import face_recognition
import os



def cc_location():
    cc = "C:/Users/HOMME/OneDrive/Desktop/universidad/python/django/facial/media/"
    return cc

def selfie_location():
    selfie = "C:/Users/HOMME/OneDrive/Desktop/universidad/python/django/facial/media/"
    return selfie


def location(func):
    location = func()
    return location


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

def valida_caso(request, id):
    respuesta= ""
    dato = get_object_or_404(Persona, pk=id)
    dato= id  
    for e in Persona.objects.filter(id=dato):        
        cc1 = e.url_documento.name
        slef1= e.url_selfi.name
        cc= location(cc_location) + cc1
        self= location(selfie_location) + slef1
        img = face_recognition.load_image_file(cc)
        try:
            Cedula1 = face_recognition.face_encodings(img)[0]
            known_encodings = [
            Cedula1
        ] 
            img2 = face_recognition.load_image_file(self)
            selfie = face_recognition.face_encodings(img2)[0]
            face_distances = face_recognition.face_distance(known_encodings, selfie)
            for i, face_distance in enumerate(face_distances):
                if(face_distance < 0.4):
                    respuesta="Se asegura que es la persona a un 70% ya que la distancia es menor a 0.40"
                elif(face_distance < 0.6):
                    respuesta="la confrotna facial da una distancia menor a 0.6 parece la persona pero se recomienda validar"
                else:
                    respuesta="la persona de la cedula no es la misma persona de la foto"
        except:
            respuesta="no se encuentra rostro"
    Persona.objects.filter(id=dato).update(resultado_fac=respuesta) 
    return redirect('consulta')