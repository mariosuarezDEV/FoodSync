from django.shortcuts import render

# Modelos
from categoria.models import ModelCategoria
from grupo.models import ModelGrupo
from producto.models import Producto
# Create your views here.

def menu(request):
    return render(request, 'inicio.html')