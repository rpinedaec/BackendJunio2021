from django.db import models

from django.db.models.expressions import OrderBy

# Create your models here.

class Auto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    imagen = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('nombre',)

class Marca(models.Model):

    BMW = 'bmw'
    CITROEN = 'citroen'
    FERRARI = 'ferrari'
    FORD = 'ford'
    MERCEDES = 'mercedes'
    PORSCHE = 'porsche'
    RENAULT = 'renault'
    TESLA = 'tesla'
    TOYOTA = 'toyota'
    VOLKSWAGEN = 'Volkswagen'

    CATEGORIES_CHOICES = (
        (BMW, 'Bmw'),
        (CITROEN, 'Citroen'),
        (FERRARI, 'Ferrari'),
        (FORD, 'Ford'),
        (MERCEDES, 'Mercedes'),
        (PORSCHE, 'Porsche'),
        (RENAULT, 'Renault'),
        (TESLA, 'Tesla'),
        (TOYOTA, 'Toyota'),
        (VOLKSWAGEN, 'Volkswagen'),
    )

    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    imagen = models.ImageField(null=True, blank=True)
    marca = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nombre',)

class Modelo(models.Model):

    DEPORTIVO = 'deportivo'
    HATCHBACK = 'Hatchback'
    SUV = 'suv'
    SEDAN = 'sedan'

    CATEGORIES_CHOICES = (
        (DEPORTIVO, 'Deportivo'),
        (HATCHBACK, 'Hatchback'),
        (SUV, 'Suv'),
        (SEDAN, 'Sedan'),
    )
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    modelo = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nombre',)