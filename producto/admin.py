from django.contrib import admin
from .models import Producto as ModelProducto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'fecha_creacion', 'fecha_actualizacion', 'estado',)
    search_fields = ('nombre',)
    list_filter = ('estado','grupo','subgrupo', 'grupo__categoria',)
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_actualizacion'

admin.site.register(ModelProducto, ProductoAdmin)
