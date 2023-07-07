from django.shortcuts import render, redirect
from .models import usuario
from django.contrib import messages
from django.contrib.auth import logout
from .forms import usuariosform
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError



# Create your views here.

def index(request):
    return render(request, "index.html")
def andres(request):
    return render(request, 'andres.html')
def camilo(request):
    return render(request, "camilo.html")
def juan(request):
    return render(request, "juan.html")
def martina(request):
    return render(request, "martina.html")
def sofia(request):
    return render(request, "sofia.html")

def artistas(request):
    return render(request, 'Artistas.html')
def productos(request):
    return render(request, 'productos.html')


def formulariolist(request):
    artistas = usuario.objects.all()
    messages.success(request, '¡artistas Listados!')
    return render(request, 'formulariolist.html')




def formulariocreate(request):
    usuario = usuariosform(request.POST or None, request.FILES or None)
    if usuario.is_valid():
       usuario.save()
       return redirect('formulariocreate')
    return render(request, "formulariocreate.html", {"artistas": artistas})






def formulariomod(request, ID_usuario):
    artistas = usuario.objects.get(ID_usuario=ID_usuario)
    usuario = usuariosform(request.POST or None, request.FILES or None, instance=artistas)
    if usuario.is_valid() and request.method == 'POST':
        usuario.save()
        return redirect('formulariomod')
    return render(request, "formulariomod.html", {"formulario": artistas})




def formulariodelete(request, ID_usuario):
    artistas = usuario.objects.get(ID_usuario=ID_usuario)
    usuario.delete()
    messages.success(request, '¡Artículo Eliminado!')
    return redirect(request, 'formulariodelete.html')

def borrarservicio(request, ID_servicio):
    servicios = Servicios.objects.get(ID_servicio = ID_servicio)
    servicios.delete()
    messages.success(request, '¡Servicio Eliminado!')
    return redirect('gestionser')