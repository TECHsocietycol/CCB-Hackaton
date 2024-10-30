from django.db import models

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    radio_geografico = models.DecimalField(max_digits=7, decimal_places=2)  # Kilómetros

    def __str__(self):
        return self.nombre


class Local(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=20, decimal_places=2)  # Aumentado a max_digits=20
    area = models.DecimalField(max_digits=15, decimal_places=2)  # Aumentado para áreas grandes
    localidad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo



class PreferenciasUsuario(models.Model):
    precio_min = models.DecimalField(max_digits=20, decimal_places=2)
    precio_max = models.DecimalField(max_digits=20, decimal_places=2)
    area_min = models.DecimalField(max_digits=15, decimal_places=2)
    area_max = models.DecimalField(max_digits=15, decimal_places=2)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Preferencias: {self.localidad} - Precio: {self.precio_min} a {self.precio_max}"
