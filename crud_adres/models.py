from django.db import models

# Creación de: 'Acquisitions'
class Acquisition(models.Model):
    budget = models.BigIntegerField(default=0) # Presupuesto
    administrative_unit = models.CharField(max_length=255) # Unidad administrativa responsable
    type_of_goods_or_services = models.CharField(max_length=255) # Tipo de bien o de servicio
    quantity = models.BigIntegerField(default=0) # Cantidad
    unit_value = models.BigIntegerField(default=0) # Valor unitario
    total_value = models.CharField(max_length=255)
    acquisition_date = models.CharField(max_length=255) # Fecha de la adquisición
    supplier = models.CharField(max_length=255) # Entidad proveedora
    documentation = models.TextField() # Documentos
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) # Fecha de última actualización
    disabled_at = models.DateTimeField(null=True, blank=True) # Fecha de desactivación

    class Meta:
        db_table = 'acquisitions' # Nombre de la tala en la DB
