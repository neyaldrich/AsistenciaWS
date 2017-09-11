from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restApi.models import Operador, Asistencia
from restApi.serializers import OperadorSerializer, AsistenciaSerializer

@api_view(['GET', 'POST'])
def operador_list(request):

    # Lista todos los operadores
    if request.method == 'GET':
        operadores = Operador.objects.all()
        serializer = OperadorSerializer(operadores, many=True)
        return Response(serializer.data)

    # Crea un nuevo operador
    elif request.method == 'POST':
        serializer = OperadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def operador_detail(request, pk):
    """
    Obtener, actualizar o eliminar un operador.
    """

    try:
        operador = Operador.objects.get(pk=pk)
    except Operador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OperadorSerializer(operador)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OperadorSerializer(operador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def asistencia_list(request):
    """
    Lista todos las asistencias o crea una nueva.
    """

    if request.method == 'GET':
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def asistencia_detail(request, pk):
    """
    Obtener una asistencia.
    """

    try:
        asitencia = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AsistenciaSerializer(asistencia)
        return Response(serializer.data)

    # No deberia ser posible modificar o eliminar una Asistencia desde la app.
