from django.urls import path
from rest_framework import routers
from .viewsets import ProductoViewSet

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

urlpatterns = router.urls