from rest_framework import serializers
from .models import ModelCategoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCategoria
        fields = '__all__'
        depth = 1
        