# miapp/views.py

from django.shortcuts import render

def my_view(request):
    # Datos de ejemplo para estadísticas con colores
    stats = [
        {'name': 'Stat 1', 'value': 75, 'color': '#4CAF50'},
        {'name': 'Stat 2', 'value': 50, 'color': '#2196F3'},
        {'name': 'Stat 3', 'value': 90, 'color': '#FF9800'},
        {'name': 'Stat 4', 'value': 60, 'color': '#F44336'}
    ]
    return render(request, 'miapp/mi_plantilla.html', {'stats': stats})
