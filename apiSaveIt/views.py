# Imports necessários de módulos a serem utilizados no projeto

from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.response import Response

from rest_framework.response import Response

from . import serializers
from rest_framework import viewsets
from .models import Categoria, SubCategoria, Planeamento, Conta, Invest, Registo, Alert
from .serializers import CategoriaSerializer, SubCategoriaSerializer, PlaneamentoSerializer, ContaSerializer, \
    InvestSerializer, RegistoSerializer, AlertSerializer, UserSerializer, UserSerializerWithToken

from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

# perfil_response = openapi.Response('Descrição da resposta', serializers.PerfilSerializer)
# @swagger_auto_schema(method='get', responses={200: perfil_response})
# @swagger_auto_schema(method='post',responses={200: perfil_response})
#

# Function based view para a criação de um perfil de um utilizador
# Transforma num ficheiro Json e depois envia para a BD

# @api_view(['GET', 'POST'])
#
# def criar_perfil(request):
#     """
#     GET: Retorna todos os perfis
#     POST: Cria um novo perfil
#     """
#     if request.method == 'GET':
#         perfis = Perfil.objects.all()
#         serializer = serializers.PerfilSerializer(perfis, many=True)
#         # print(serializer.data)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = serializers.PerfilSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
# def perfil_detalhe(request, perfil_id):
#     """
#     GET: Retorna um perfil baseado num ID
#     PATCH: Altera um perfil baseado num ID
#     DELETE: Elimina um perfil baseado num ID
#     """
#     try:
#         perfil = Perfil.objects.get(pk=perfil_id)
#     except Perfil.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = serializers.PerfilSerializer(perfil)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'DELETE':
#         perfil.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT)
#

categoria_response = openapi.Response('Descrição da resposta', serializers.CategoriaSerializer)


@swagger_auto_schema(method='get', responses={200: categoria_response}, )
@swagger_auto_schema(method='post', responses={200: categoria_response})
@api_view(['GET', 'POST'])
def criar_categoria(request):
    """
    GET: Retorna todas as categorias
    POST: Insere uma nova categoria
    """
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
    # return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def categoria_detalhe(request, categoria_id):
    """
    GET: Retorna as categorias baseado num ID
    PATCH: Altera uma categoria baseado num ID
    DELETE: Apaga uma categoria baseado num ID
    """
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CategoriaSerializer(categoria)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        categoria.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_subcategoria(request):
    """
    GET: Retorna todas as sub_categorias
    POST: Insere uma nova sub_categoria
    """
    if request.method == 'GET':
        sub_categorias = SubCategoria.objects.all()
        serializer = serializers.SubCategoriaSerializer(sub_categorias, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.SubCategoriaPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def subcategoria_detalhe(request, sub_categoria_id):
    """
    GET: Retorna as subcategorias baseado num ID
    PATCH: Altera uma subcategoria baseado num ID
    DELETE: Apaga uma subcategoria baseado num ID
    """
    try:
        sub_categoria = SubCategoria.objects.get(pk=sub_categoria_id)
    except SubCategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.SubCategoriaSerializer(sub_categoria)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        sub_categoria.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_planeamento(request):
    """
    GET: Retorna todos os planeamentos
    POST: Insere um novo planeamento
    """
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


def planeamento_detalhe(request, planeamento_id):
    """
    GET: Retorna o planeamento baseado num ID
    PATCH: Atualiza um planeamento baseado num ID
    DELETE: Apaga um planeamento baseado num ID
    """
    try:
        planeamento = Planeamento.objects.get(pk=planeamento_id)
    except Planeamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PlaneamentoSerializer(planeamento)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        planeamento.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_conta(request):
    """
    GET: Retorna todas as contas
    POST: Insere uma nova conta
    """
    if request.method == 'GET':
        contas = Conta.objects.all()
        serializer = serializers.ContaSerializer(contas, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.ContaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def conta_detalhe(request, conta_id):
    """
    GET: Retorna a conta baseado num ID
    PATCH: Atualiza a conta baseado num ID
    DELETE: Apaga a conta baseado num ID
    """
    try:
        contas = Conta.objects.get(pk=conta_id)
    except Conta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ContaSerializer(contas)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        contas.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_invest(request):
    """
    GET: Retorna todos os investimentos
    POST: Cria um novo investimento
    """
    if request.method == 'GET':
        invest = Invest.objects.all()
        serializer = serializers.InvestSerializer(invest, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.InvestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def invest_detalhe(request, invest_id):
    """
    GET: Retorna um registo baseado num ID
    PATCH: Altera um registo baseado num ID
    DELETE: Elimina um registo baseado num ID
    """
    try:
        invest = Invest.objects.get(pk=invest_id)
    except Invest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.InvestSerializer(invest)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        invest.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_registo(request):
    """
    GET: Retorna todos os registos
    POST: Cria um novo registo
    """
    if request.method == 'GET':
        registo = Registo.objects.all()
        serializer = serializers.RegistoSerializer(registo, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.RegistoPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def registo_detalhe(request, registo_id):

    """
    GET: Retorna um registo baseado num ID
    PATCH: Altera um registo baseado num ID
    DELETE: Elimina um registo baseado num ID
    """
    try:
        registo = Registo.objects.get(pk=registo_id)
    except Invest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.RegistoSerializer(registo)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        registo.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_alert(request):
    """
    GET: Retorna todos os alertas
    POST: Cria um novo alertas
    """
    if request.method == 'GET':
        alert = Registo.objects.all()
        serializer = serializers.AlertSerializer(alert, many=True)
        # print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.AlertPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def alert_detalhe(request, alert_id):
    """
    GET: Retorna um alerta baseado num ID
    PATCH: Altera um alerta baseado num ID
    DELETE: Elimina um alerta baseado num ID
    """
    try:
        alert = Alert.objects.get(pk=alert_id)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.RegistoSerializer(alert)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        alert.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class SubCategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriaSerializer
    queryset = SubCategoria.objects.all()


class PlaneamentoViewSet(viewsets.ModelViewSet):
    serializer_class = PlaneamentoSerializer
    queryset = Planeamento.objects.all()


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()


class InvestViewSet(viewsets.ModelViewSet):
    serializer_class = InvestSerializer
    queryset = Invest.objects.all()


class RegistoViewSet(viewsets.ModelViewSet):
    serializer_class = RegistoSerializer
    queryset = Registo.objects.all()


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
