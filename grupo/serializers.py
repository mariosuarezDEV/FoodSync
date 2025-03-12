from rest_framework import serializers
from .models import ModelGrupo
from .models import ModelSubGrupo
from categoria.serializers import CategoriaSerializer

class GrupoSerializer(serializers.ModelSerializer):  # Importante: many=True para M2M
    class Meta:
        model = ModelGrupo
        fields = [
            'id',
            'nombre',
            'categoria',
            'fecha_creacion',
            'fecha_actualizacion',
            'estado'
        ]
        depth = 1
        
    
class SubGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSubGrupo
        fields = '__all__'
        depth = 1