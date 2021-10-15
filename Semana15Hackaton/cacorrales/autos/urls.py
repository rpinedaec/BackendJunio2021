from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from autos import views

router = DefaultRouter()
router.register(r'auto', views.AutoViewSet)
router.register(r'marca', views.MarcaViewSet)
router.register(r'modelo', views.ModeloViewSet)
urlpatterns = [
    path('', include(router.urls))
]