from django.urls import path
from django.urls.resolvers import URLPattern
from alumno import views

app_name = 'alumno'

urlpatterns = [
    path('inicio', views.home, name='home'),
]