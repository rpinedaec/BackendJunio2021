from django.db import models
from django.db.models.base import Model

# Create your models here.

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.nombres

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    nota1 = models.IntegerField(2)
    nota2 = models.IntegerField(2)
    nota3 = models.IntegerField(2)
    nota4 = models.IntegerField(2)
    nota5 = models.IntegerField(2) 
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descripcion