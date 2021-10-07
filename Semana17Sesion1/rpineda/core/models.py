from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class costumer(models.Model):
    centro = models.CharField(max_length=3)
    tipo_almacen = models.CharField(max_length=50)
    cod_material = models.CharField(max_length=9)
    desc_material = models.CharField(max_length=500)
    unidad = models.CharField(max_length=10)
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)

    def __str__(self):
        return self.name