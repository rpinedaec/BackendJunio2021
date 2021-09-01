from django.contrib import admin
from profesor.models import Profesor, Asistencia

# Register your models here.

class ProfesorAdmin(admin.ModelAdmin):
    
    list_display=("nombres", "apellidos", "correo")
    search_fields=("nombres", "apellidos")

class ProfesorAsistencia(admin.ModelAdmin):

    list_display=("lunes", "martes", "miercoles", "jueves", "viernes")

admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Asistencia,ProfesorAsistencia)
