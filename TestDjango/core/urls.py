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
    

    #crud
    path('formulariolist/', views.formulariolist, name='formulariolist'),
    path('formulariocreate/', views.formulariocreate, name='formulariocreate'),
    path('formulariomod/', views.formulariomod, name='formulariomod'),
    path('formulariodelete/', views.formulariodelete, name='formulariodelete'),

    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('accounts/profile/', views.profile_view, name='profile'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

