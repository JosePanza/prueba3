from django.forms import ModelForm
from django import forms
from .models import usuario

class usuariosform(forms.ModelForm):
    class Meta:
        model = usuario 
        #fields = ['ID', 'Nombre', 'Encargado', 'Tipo de Servicio', 'fecha_creacion'] 
   
        fields = '__all__' 