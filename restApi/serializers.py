from rest_framework import serializers
from restApi.models import Operador, Asistencia, Administrador

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', 'apellido', 'cedula', 'telefono', 'faceData')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('operador', 'latitud', 'longitud', 'fecha', 'hora', 'isEntrada')

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('username', 'password')
