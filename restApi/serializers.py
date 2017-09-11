from rest_framework import serializers
from restApi.models import Operador, Asistencia

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', 'apellido', 'cedula', 'telefono', 'faceData')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('operador', 'latitud', 'longitud', 'fecha', 'isEntrada')
