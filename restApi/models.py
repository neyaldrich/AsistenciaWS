from django.db import models
from rest_framework import serializers

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')

class Operador(models.Model):
    idOperador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, default='')
    apellido = models.CharField(max_length=100, blank=False, default='')
    cedula = models.CharField(max_length=10, blank=False, default='')
    telefono = models.CharField(max_length=10, blank=True, default='')
    foto1 = models.TextField(blank=True, null=True, default="")
    foto2 = models.TextField(blank=True, null=True, default="")
    foto3 = models.TextField(blank=True, null=True, default="")
    foto4 = models.TextField(blank=True, null=True, default="")
    foto5 = models.TextField(blank=True, null=True, default="")


class Asistencia(models.Model):
    idOperador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=100, blank=True, default='')
    longitud = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateField(auto_now_add=False)
    hora = models.TimeField(auto_now_add=False)
    isEntrada = models.BooleanField(default=True)
