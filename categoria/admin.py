from django.contrib import admin
from .models import ModelCategoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado',)
    search_fields = ('nombre',)
    list_filter = ('estado',)
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_actualizacion'


admin.site.register(ModelCategoria, CategoriaAdmin)