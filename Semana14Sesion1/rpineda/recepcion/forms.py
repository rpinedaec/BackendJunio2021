from django import forms
from django.forms import widgets
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres','apellidos','nacionalidad', 'descripcion']
        labels = {
            'nombres': 'Nombres del Cliente',
            'apellidos': 'Apellidos del Cliente',
            'nacionalidad': 'Nacionalidad del Cliente',
            'descripcion': 'Descripcion del Cliente'
        }
        widgets={
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingresa los nombres del Cliente',
                    'id':'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingresa los apellidos del Cliente',
                    'id':'apellidos'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingresa la nacionalidad del Cliente',
                    'id':'nacionalidad'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingresa la descripcion del Cliente',
                    'id':'descripcion'
                }
            ),

        }