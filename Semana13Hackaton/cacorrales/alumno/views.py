from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def asistencia_alumno(request):

    return render(request, "asistencia_alumno.html")

def marcado(request):

    mensaje="Asistencia en Estado: %r" %request.GET["estado"]

    return HttpResponse(mensaje)