from django.db import models
from categoria.models import ModelCategoria

# Create your models here.
class ModelGrupo(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre del grupo")
    categoria = models.ManyToManyField(ModelCategoria, verbose_name="Categoria ", blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion", blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion", blank=False, null=False)
    estado = models.BooleanField(default=True,verbose_name="Estado del grupo", blank=False, null=False)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        db_table = "grupo"

class ModelSubGrupo(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre del subgrupo")
    grupo = models.ForeignKey(ModelGrupo, on_delete=models.CASCADE, verbose_name="Grupo", blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion", blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion", blank=False, null=False)
    estado = models.BooleanField(default=True,verbose_name="Estado del subgrupo", blank=False, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Sub grupo"
        verbose_name_plural = "Sub Grupos"
        db_table = "subgrupo"