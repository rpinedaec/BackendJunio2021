from django.shortcuts import render
from .models import Auto, Marca, Modelo
from .serializers import AutoSerializer, MarcaSerializer, ModeloSerializer
from rest_framework import viewsets, filters

# Create your views here.

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('marca',)

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('modelo',)
