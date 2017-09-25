from restApi.models import Operador, Asistencia, Administrador
from restApi.serializers import OperadorSerializer, AsistenciaSerializer, AdministradorSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view

class AdministradorList(APIView):

    # Lista todos los admins
    def get(self,request, format=None):
        administradores = Administrador.objects.all()
        serializer = AdministradorSerializer(administradores, many=True)
        return Response(serializer.data)

class OperadorList(APIView):

    # Lista todos los operadores
    def get(self,request, format=None):
        operadores = Operador.objects.all()
        serializer = OperadorSerializer(operadores, many=True)
        return Response(serializer.data)

    # Crea un nuevo operador
    def post(self, request, format=None):
        serializer = OperadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OperadorDetail(APIView):
    """
    Obtener, actualizar o eliminar un operador.
    """

    def get_object(self, pk):
        try:
            return Operador.objects.get(pk=pk)
        except Operador.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        operador = self.get_object(pk)
        serializer = OperadorSerializer(operador)
        return Response(serializer.data)

    def put(self, request, pk,  format=None):
        operador = self.get_object(pk)
        serializer = OperadorSerializer(operador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        operador = self.get_object(pk)
        operador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AsistenciaList(APIView):
    """
    Lista todos las asistencias o crea una nueva.
    """

    def get(self, request, format=None):
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AsistenciaDetail(APIView):
    """
    Obtener una asistencia.
    """

    def get_object(self, pk):
        try:
            return Asistencia.objects.get(pk=pk)
        except Asistencia.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        asistencia = self.get_object(pk)
        serializer = AsistenciaSerializer(asistencia)
        return Response(serializer.data)

    # No deberia ser posible modificar o eliminar una Asistencia desde la app.

# REPORTES
#
# @api_view(['GET'])
# def asistenciasOperador(request):
