from django.db import models

class Registrado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, blank=True)  # Campo opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
