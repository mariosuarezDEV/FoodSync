from django.urls import path
from rest_framework import routers
from .viewsets import GrupoViewSet
from .viewsets import SubGrupoViewSet

router = routers.DefaultRouter()
router.register('grupos', GrupoViewSet)
router.register('subgrupos', SubGrupoViewSet)

urlpatterns = router.urls
