from django.db import models
from django.urls import reverse

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        return self.nombre