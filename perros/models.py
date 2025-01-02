from django.db import models
from datetime import timedelta, date

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    madre = models.CharField(max_length=100)
    padre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cruce(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, related_name="cruces")
    fecha_insem = models.DateField()
    fecha_actual = models.DateField(auto_now=True)
    dias_transcurridos = models.PositiveIntegerField(blank=True, null=True)
    fecha_parto_estimada = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.dias_transcurridos = (date.today() - self.fecha_insem).days
        self.fecha_parto_estimada = self.fecha_insem + timedelta(days=63)
        super().save(*args, **kwargs)