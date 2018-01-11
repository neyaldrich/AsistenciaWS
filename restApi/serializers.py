from rest_framework import serializers
from restApi.models import Operador, Asistencia, Admin, TipoUsuario, Proyecto, ProyectoOperador

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('idOperador', 'nombre', 'apellido', 'cedula', 'telefono', 'foto1', 'foto2', 'foto3', 'foto4', 'foto5','estado','idTipoUsuario')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia

        fields = ('id', 'idOperador', 'latitud', 'longitud', 'fecha', 'hora', 'isEntrada')
        hora = serializers.TimeField(format="%H:%M")

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('idTipoUsuario', 'nombre','estado')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('idProyecto', 'nombre','estado')

class ProyectoOperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoOperador
        fields = ('idProyectoOperador', 'idProyecto','idOperador','estado')



