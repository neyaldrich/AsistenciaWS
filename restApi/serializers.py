from rest_framework import serializers
from restApi.models import Operador, Asistencia, Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', 'apellido', 'cedula', 'telefono', 'encodedFaceData')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('operador', 'latitud', 'longitud', 'fecha', 'hora', 'isEntrada')
