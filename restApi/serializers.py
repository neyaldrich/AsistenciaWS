from rest_framework import serializers
<<<<<<< Updated upstream
from restApi.models import Operador, Asistencia, Administrador
=======
from restApi.models import Operador, Asistencia, Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')
>>>>>>> Stashed changes

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', 'apellido', 'cedula', 'telefono', 'encodedFaceData')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('operador', 'latitud', 'longitud', 'fecha', 'hora', 'isEntrada')
<<<<<<< Updated upstream

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('username', 'password')
=======
>>>>>>> Stashed changes
