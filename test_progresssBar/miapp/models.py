# miapp/models.py

from django.db import models

class Stat(models.Model):
    name = models.CharField(max_length=150)
    value = models.PositiveIntegerField()  # El porcentaje, entre 0 y 100
    color = models.CharField(max_length=7)  # Código de color hex (#FFFFFF)

    def __str__(self):
        return self.name
