from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural  = 'Clientes'
        ordering = ['nombres','apellidos']

    def __str__(self) -> str:
        return self.nombres


