from django.urls import path
from .views import index
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', index, name='index'),
    path('andres', views.andres , name='andres'),
    path('camilo', views.camilo, name='camilo'),
    path('juan', views.juan, name='juan'),
    path('martina', views.martina, name='martina'),   
    path('sofia', views.sofia, name='sofia'),  
    path('artistas', views.artistas, name='artistas'),
    path('productos', views.productos, name='productos'),

    #crud
    path('formulariolist', views.formulariolist, name='formulariolist'),
    path('formulariocreate', views.formulariocreate, name='formulariocreate'),
    path('formulariomod', views.formulariomod, name='formulariomod'),
    path('formulariodelete', views.formulariodelete, name='formulariodelete')

    

] 

