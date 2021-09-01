from django.urls import path
from .views import BorrarCliente, home, ListarClientes, CrearCliente, ActualizarCliente

app_name='recepcion'
urlpatterns = [
    path('', home.as_view(), name='index'),
    path('listar_clientes', ListarClientes.as_view(), name='listar_clientes'),
    path('crear_clientes', CrearCliente.as_view(), name='crear_cliente'),
    path('<pk>/actualizar_clientes', ActualizarCliente.as_view(), name='actualizar_cliente'),
    path('<pk>/borrar_clientes', BorrarCliente.as_view(), name='borrar_cliente')
]