from django.contrib import admin
from .models import ModelGrupo, ModelSubGrupo
# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado',)
    search_fields = ('nombre',)
    list_filter = ('estado', 'categoria',)
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_actualizacion'
    

class SubGrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'grupo__nombre', 'fecha_creacion', 'fecha_actualizacion', 'estado',)
    search_fields = ('nombre',)
    list_filter = ('estado', 'grupo',)
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_actualizacion'

admin.site.register(ModelGrupo, GrupoAdmin)
admin.site.register(ModelSubGrupo, SubGrupoAdmin)