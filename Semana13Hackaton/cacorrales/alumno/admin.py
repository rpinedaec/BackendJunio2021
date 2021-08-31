from django.contrib import admin
from alumno.models import Alumno, Curso

# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    
    list_display=("nombres", "apellidos", "correo")
    search_fields=("nombres", "apellidos")

class AlumnoCurso(admin.ModelAdmin):

    list_display=("descripcion", "alumno", "nota1", "nota2", "nota3", "nota4", "nota5")

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Curso,AlumnoCurso)
