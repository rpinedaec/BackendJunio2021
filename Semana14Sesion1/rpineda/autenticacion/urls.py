from django.urls import path, include
from autenticacion.views import Login
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]