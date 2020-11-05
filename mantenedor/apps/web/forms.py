from django import forms
from django.forms import ModelForm
from .models import Alumno


class registroForm(forms.ModelForm):
        class Meta:
                model = Alumno
                fields = '__all__' 



       
   

# class registroForm(forms.ModelForm):

#     class meta:
#         model = Alumno
        # fields = ['nombre','apellido','rut','email','contrasena']



# class formulario(forms.Form):
#         model = Alumno