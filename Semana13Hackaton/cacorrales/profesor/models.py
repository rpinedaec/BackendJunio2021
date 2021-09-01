from django.contrib.admin.helpers import checkbox
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.nombres

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    lunes = models.BooleanField
    martes = models.BooleanField
    miercoles = models.BooleanField
    jueves = models.BooleanField
    viernes = models.BooleanField

    def __str__(self) -> str:
        return self.lunes
