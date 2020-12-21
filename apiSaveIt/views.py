#Imports necessários de módulos a serem utilizados no projeto

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from .models import Perfil, Categoria, SubCategoria, Planeamento
from .serializers import PerfilSerializer, CategoriaSerializer, SubCategoriaSerializer, PlaneamentoSerializer

from django.http import Http404
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

perfil_response = openapi.Response('Descrição da resposta', serializers.PerfilSerializer)
@swagger_auto_schema(method='get', responses={200: perfil_response},)
@swagger_auto_schema(method='post',responses={200: perfil_response})


#Function based view para a criação de um perfil de um utilizador. Transforma num ficheiro Json e depois envia para a BD

@api_view(['GET', 'POST'])

def criar_perfil(request):
    """
    get: Retorna todos os perfis, baseado em function based views
    post: Cria um novo perfil, baseado em function based views
    """
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
def perfil_detalhe(request, perfil_id):
    """
    get: Retorna um perfil
    post: Atualiza um perfil baseado num ID
    delete: Elimina um perfil baseado num ID
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


@api_view(['GET', 'POST', 'DELETE'])

def criar_categoria(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = serializers.CategoriaSerializer(categorias, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    #return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})

def categoria_detalhe(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_subcategoria(request):
    if request.method == 'GET':
        sub_categorias = SubCategoria.objects.all()
        serializer = serializers.SubCategoriaSerializer(sub_categorias, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.SubCategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def criar_planeamento(request):
    if request.method == 'GET':
        planeamentos = Planeamento.objects.all()
        serializer = serializers.PlaneamentoSerializer(planeamentos, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.PlaneamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def planeamento_detalhe(request, planeamento_id):
    try:
        planeamento = Planeamento.objects.get(pk=planeamento_id)
    except Planeamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PlaneamentoSerializer(planeamento)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        planeamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class SubCategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriaSerializer
    queryset = SubCategoria.objects.all()

class PlaneamentoViewSet(viewsets.ModelViewSet):
    serializer_class = PlaneamentoSerializer
    queryset = Planeamento.objects.all()


