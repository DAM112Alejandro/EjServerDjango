from django.db import models

# Create your models here.

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    ingeniero = models.CharField(max_length=100)
    victoria = models.IntegerField()
    años = models.IntegerField()
    numero = models.IntegerField()

    
    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

