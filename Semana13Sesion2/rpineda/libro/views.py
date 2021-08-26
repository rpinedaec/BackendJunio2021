from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from .forms import AutorForm

# Create your views here.
def Home(request):
    return render(request, 'libro/index.html')

@require_http_methods(["POST","GET"])
def crear_autor(request):
    if request.method == 'POST':
        autor_forms = AutorForm(request.POST)
        if autor_forms.is_valid():
            autor_forms.save()
            return redirect('index')
    else:
        autor_forms = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_forms' : autor_forms })

    

