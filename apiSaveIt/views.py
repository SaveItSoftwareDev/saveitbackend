from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
# Create your views here.


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from .models import Perfil, Categoria
from .serializers import PerfilSerializer, CategoriaSerializer

from django.http import Http404
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

perfil_response = openapi.Response('Descrição da resposta', serializers.PerfilSerializer)
@swagger_auto_schema(method='get', responses={200: perfil_response},)
@swagger_auto_schema(method='post',responses={200: perfil_response})

@api_view(['GET', 'POST'])

def criar_perfil(request):
    if request.method == 'GET':
        perfis = Perfil.objects.all()
        serializer = serializers.PerfilSerializer(perfis, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.PerfilSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'DELETE'])
def perfil_detail(request, perfil_id):
    """
    get: Retorna um restaurante (com function based views)
    put: Atualiza um novo restaurante (com function based views)
    delete: Elimina um restaurante (com function based views).
    """
    try:
        perfil = Perfil.objects.get(pk=perfil_id)
    except Perfil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PerfilSerializer(perfil)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


categoria_response = openapi.Response('Descrição da resposta', serializers.CategoriaSerializer)
@swagger_auto_schema(method='get', responses={200: categoria_response},)
@swagger_auto_schema(method='post',responses={200: categoria_response})


@api_view(['GET', 'POST'])

def criar_categoria(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = serializers.CategoriaSerializer(categorias, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()


