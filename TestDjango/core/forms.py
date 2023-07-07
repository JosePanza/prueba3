from django.forms import ModelForm
from django import forms
from .models import user

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = user 
        #fields = ['ID', 'Nombre', 'Encargado', 'Tipo de Servicio', 'fecha_creacion'] 
   
        fields = '__all__' 