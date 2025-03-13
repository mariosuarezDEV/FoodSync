from .models import ModelCategoria

def categorias_context(request):
    return {'categorias': ModelCategoria.objects.filter(estado=True)}