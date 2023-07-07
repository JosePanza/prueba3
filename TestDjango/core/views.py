from django.shortcuts import render, redirect
from .models import usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



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
    return render(request, 'formulariolist.html', {'user': usuario})


def formulariocreate(request):
    if request.method == 'POST':
        ID_artista = request.POST['ID_artista']
        nombre_artista = request.POST['nombre_artista']
        descripcion = request.POST['descripcion']
        img = request.FILES['img']
        artistas = usuario(ID_artista=ID_artista, nombre_artista=nombre_artista, descripcion=descripcion, img=img)
        artistas.save()
        messages.success(request, '¡Artista Registrado!')
        return redirect('formulariolist')
    return render(request, 'formulariocreate.html')


def formulariomod(request):
    artistas = usuario.objects.all()
    if request.method == 'POST':
        artistas = usuario.objects.get(id=request.POST['artista_id'])
        artistas.nombre_usuario = request.POST['nombre_artista']
        artistas.descripcion = request.POST['descripcion']
        artistas.img = request.POST['img']
        artistas.save()
        messages.success(request, '¡Artista Actualizado!')
        return redirect('formulariolist')
    return render(request, 'formulariomod.html')


def formulariodelete(request):
    artistas = usuario.objects.all()
    if request.method == 'POST':
        ID_usuario  = request.POST['artista_id']
        artista = usuario.objects.get(id=ID_usuario )
        artista.delete()
        messages.success(request, '¡Artista Eliminado!')
        return redirect('formulariolist')
    return render(request, 'formulariodelete', {'artistas': usuario})