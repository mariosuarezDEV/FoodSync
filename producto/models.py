from django.db import models
from grupo.models import ModelGrupo, ModelSubGrupo

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre del producto")
    descripcion = models.TextField(max_length=500, blank=True, null=True, verbose_name="Descripción del producto")
    grupo = models.ForeignKey(ModelGrupo, on_delete=models.PROTECT, verbose_name="Grupo del producto", blank=False, null=False)
    subgrupo = models.ForeignKey(ModelSubGrupo, on_delete=models.PROTECT, verbose_name="Subgrupo del producto", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del producto", blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Stock del producto", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", blank=False, null=False)
    estado = models.BooleanField(default=True, verbose_name="Estado del producto", blank=False, null=False)

    def __str__(self):
        return f'{self.nombre} - {self.grupo} - {self.subgrupo}'
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "producto"