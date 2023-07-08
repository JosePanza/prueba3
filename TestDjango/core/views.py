
from .models import usuario
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from .forms import usuariosform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User




@login_required
def profile_view(request):
   
    user = request.user
    
   
    
    context = {
        'user': user,
        
    }
    
    return render(request, 'profile.html', context)


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
def login (request):
    return render(request, "login.html")

def formulariolist(request):
    artistas = usuario.objects.all()
    messages.success(request, '¡artistas Listados!')
    return render(request, 'formulariolist.html')
def formulariocreate(request):
    usuario = usuariosform(request.POST or None, request.FILES or None)
    if usuario.is_valid():
        usuario.save()
        messages.success(request,'¡artistas agregado!')
        return redirect('formulariocreate')
    return render(request, "formulariocreate.html", {"artistas": artistas})
def formulariomod(request, ID_usuario):
    artistas = usuario.objects.get(ID_usuario=ID_usuario)
    formulario = usuariosform(request.POST or None, request.FILES or None, instance=artistas)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('formulariomod')
    return render(request, "formulariomod.html", {"artista": artistas})
def formulariodelete(request):
    artistas = usuario.objects.filter()
    artistas.delete()
    messages.success(request, '¡artista Eliminado!')
    return render(request, 'formulariodelete.html', {'artistas': artistas})
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Nombre de usuario o contraseña incorrectos'})
        else:
            auth_login(request, user)
            return redirect('index')
def registro_view(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                    username=request.POST['username'],
                    password =request.POST['password1'])
                    user.save()
                    login(request)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error" : 'Usuario ya existe'
                })
            
        return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error" : 'La contraseña no coincide'
                })
def logout_view(request):
    logout(request)
    return redirect('index')
