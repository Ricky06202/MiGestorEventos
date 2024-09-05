from django.db import models


class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
