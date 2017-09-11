from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restApi.models import Operador, Asistencia
from restApi.serializers import OperadorSerializer, AsistenciaSerializer

# Create your views here.
@csrf_exempt
def operador_list(request):
    """
    Lista todos los operadores o crea uno nuevo.
    """
    if request.method == 'GET':
        operadores = Operador.objects.all()
        serializer = OperadorSerializer(operadores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OperadorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def operador_detail(request, pk):
    """
    Obtener, actualizar o eliminar un operador.
    """
    try:
        operador = Operador.objects.get(pk=pk)
    except Operador.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OperadorSerializer(operador)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OperadorSerializer(operador, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        operador.delete()
        return HttpResponse(status=204)

@csrf_exempt
def asistencia_list(request):
    """
    Lista todos las asistencias o crea una nueva.
    """
    if request.method == 'GET':
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AsistenciaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def asistencia_detail(request, pk):
    """
    Obtener una asistencia.
    """
    try:
        asitencia = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AsistenciaSerializer(asistencia)
        return JsonResponse(serializer.data)

    # No deberia ser posible modificar o eliminar una Asistencia desde la app.
