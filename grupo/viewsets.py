from rest_framework import viewsets
from .models import ModelGrupo
from .models import ModelSubGrupo
from .serializers import GrupoSerializer
from .serializers import SubGrupoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = ModelGrupo.objects.all()
    serializer_class = GrupoSerializer
    
class SubGrupoViewSet(viewsets.ModelViewSet):
    queryset = ModelSubGrupo.objects.all()
    serializer_class = SubGrupoSerializer