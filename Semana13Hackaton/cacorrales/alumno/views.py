#from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from alumno.models import Alumno
from django.contrib.auth.decorators import login_required

# Create your views here.



def asistencia_alumno(request):

    return render(request, "asistencia_alumno.html")

def asistencia(request):

    if request.GET["estado"]:

        #mensaje="Su estado de asistencia es: %r" %request.GET["estado"]
        estado = request.GET["estado"]
        
        alumnos = Alumno.objects.filter(nombres__icontains=estado)

        return render(request, "resultado_busqueda.html", {"alumnos":estado, "query":estado})
    else:
    
        mensaje="No haz ingresado tu asistencia/tardanza"

    return HttpResponse(mensaje)

@login_required

def home(request):
    return HttpResponse("Bienvenidos")