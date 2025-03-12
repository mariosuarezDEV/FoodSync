from django.urls import path
from rest_framework import routers
from .viewsets import CategoriaViewSet

router = routers.DefaultRouter()
router.register('categoria', CategoriaViewSet)

urlpatterns = router.urls

