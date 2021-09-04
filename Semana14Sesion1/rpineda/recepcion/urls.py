from django.urls import path
from .views import BorrarCliente, home, ListarClientes, CrearCliente, ActualizarCliente
from autenticacion.views import Login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name='recepcion'
urlpatterns = [
    
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home.as_view(), name='index'),
    path('listar_clientes', ListarClientes.as_view(), name='listar_clientes'),
    path('crear_clientes', login_required(CrearCliente.as_view()), name='crear_cliente'),
    path('<pk>/actualizar_clientes', ActualizarCliente.as_view(), name='actualizar_cliente'),
    path('<pk>/borrar_clientes', BorrarCliente.as_view(), name='borrar_cliente')
]