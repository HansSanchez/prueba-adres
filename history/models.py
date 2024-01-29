from django.db import models

class History(models.Model):
    action = models.TextField() # Acción realizada
    module = models.CharField(max_length=255) # Módulo en el que se hizo la acción
    description = models.TextField(null=True, blank=True) # Historial de lo que se hizo
    created_at = models.DateTimeField(auto_now_add=True) # Fecha de registro de cuando se hizo

    class Meta:
        db_table = 'histories'