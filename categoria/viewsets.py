from rest_framework import viewsets
from .models import ModelCategoria
from .serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = ModelCategoria.objects.all()
    serializer_class = CategoriaSerializer
    