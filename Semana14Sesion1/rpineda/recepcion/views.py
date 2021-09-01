from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy
# Create your views here.

class home(TemplateView):
    template_name = 'recepcion/index.html'
    
    def get_context_data(self,*agrs, **kwargs):
        clientes = Cliente.objects.all()
        context = super(home, self).get_context_data(*agrs, **kwargs)
        context['clientes'] = clientes
        return context
    
class ListarClientes(ListView):
    model=Cliente
    template_name = 'recepcion/index.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'

class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'recepcion/crear.html'
    success_url = reverse_lazy('recepcion:index')

class ActualizarCliente(UpdateView):
    model = Cliente
    fields = ['nombres', 'apellidos']
    template_name = 'recepcion/crear.html'
    success_url = reverse_lazy('recepcion:index')

class BorrarCliente(DeleteView):
    model = Cliente
    template_name = 'recepcion/borrar.html'
    success_url = reverse_lazy('recepcion:index')
    # def get(self, request, *args, **kwargs):
    #     clientes = Cliente.objects.all()
    #     return render(request, 'recepcion/index.html',{'clientes':clientes})
    # def post(self,request, *args, **kwargs):
    #     clientes = Cliente.objects.all()
    #     return render(request, 'recepcion/indexp.html',{'clientes':clientes})

    # def put(self):
    #     pass

    # def delete(self):
    #     pass