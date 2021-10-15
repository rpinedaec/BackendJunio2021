from django.db import models

# Create your models here.
class costumer(models.Model):
     centro = models.CharField(max_length=50)
     perfil = models.CharField(max_length=4)
     descripcion = models.CharField(max_length=80)
     cod_usuario = models.CharField(max_length=15)
     dni = models.CharField(max_length=15)
     apellidos_nombres = models.CharField(max_length= 80)

     def __str__(self):

         return self.centro
    