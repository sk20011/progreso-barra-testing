# miapp/views.py

from django.shortcuts import render
from .models import Stat

def my_view(request):
    # Obtener todas las estadísticas desde la base de datos
    stats = Stat.objects.all()
    return render(request, 'miapp/mi_plantilla.html', {'stats': stats})
