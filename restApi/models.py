from django.db import models
from rest_framework import serializers

# Create your models here.

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, default='')
    estado = models.CharField(max_length=3, blank=False, default='')

class Proyecto(models.Model):
    idProyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, default='')
    estado = models.CharField(max_length=3, blank=False, default='')

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
    estado = models.CharField(max_length=3, blank=True, default='')
    idTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE,null=True, default="",db_column='idTipoUsuario')	


class ProyectoOperador(models.Model):
    idProyectoOperador = models.AutoField(primary_key=True)
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null=True, default="",db_column='idProyecto')	
    idOperador = models.ForeignKey(Operador, on_delete=models.CASCADE,null=True, default="",db_column='idOperador')	
    estado = models.CharField(max_length=3, blank=False, default='')



class Asistencia(models.Model):
    idOperador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=100, blank=True, default='')
    longitud = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateField(auto_now_add=False)
    hora = models.TimeField(auto_now_add=False)
    isEntrada = models.BooleanField(default=True)



