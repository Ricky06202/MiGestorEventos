from django.db import models


# Modelo para Organizadores
class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()


# Modelo para Eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
