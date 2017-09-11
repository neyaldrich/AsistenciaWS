from django.db import models

# Create your models here.

class Admin(models.Model):
    usuario = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')

class Operador(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='')
    apellido = models.CharField(max_length=100, blank=True, default='')
    cedula = models.CharField(max_length=100, blank=True, default='')
    telefono = models.CharField(max_length=20, blank=True, default='')
    faceData = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('apellido',)

"""TODO: Separar la fecha en dos campos: fecha, hora"""

class Asistencia(models.Model):
    operador = models.ForeignKey('Operador', on_delete=models.CASCADE)
    latitud = models.CharField(max_length=100, blank=True, default='')
    longitud = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateTimeField(auto_now_add=True)
    isEntrada = models.BooleanField(default=True)
