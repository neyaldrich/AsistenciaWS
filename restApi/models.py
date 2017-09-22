from django.db import models

# Create your models here.

class Administrador(models.Model):
    username = models.CharField(max_length=100, blank=False, unique=True, default='')
    password = models.CharField(max_length=100, blank=False, default='')

class Operador(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default='')
    apellido = models.CharField(max_length=100, blank=False, default='')
    cedula = models.CharField(max_length=100, blank=False, default='')
    telefono = models.CharField(max_length=20, blank=True, default='')
    faceData = models.CharField(max_length=5000, blank=True, default='')

    class Meta:
        ordering = ('apellido',)

"""TODO: Separar la fecha en dos campos: fecha, hora"""

class Asistencia(models.Model):
    operador = models.ForeignKey('Operador', on_delete=models.CASCADE)
    latitud = models.CharField(max_length=100, blank=False, default='')
    longitud = models.CharField(max_length=100, blank=False, default='')
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    isEntrada = models.BooleanField(default=True)
