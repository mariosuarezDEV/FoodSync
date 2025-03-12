from django.db import models

# Create your models here.
class ModelCategoria(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre de la categoria")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion", blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion", blank=False, null=False)
    estado = models.BooleanField(default=True, verbose_name="Estado de la categoria", blank=False, null=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"  