# Imports necessários de módulos a serem utilizados no projeto
from django.http import JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Categoria, SubCategoria, Planeamento, Conta, Invest, Registo, Alert
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

categoria_response = openapi.Response('OK', serializers.CategoriaSerializer)
subcategoria_response = openapi.Response('OK', serializers.SubCategoriaPUTSerializer)
planeamento_response = openapi.Response('OK', serializers.PlaneamentoPUTSerializer)
conta_response = openapi.Response('OK', serializers.ContaSerializer)
investimento_response = openapi.Response('OK', serializers.InvestSerializer)
registo_response = openapi.Response('OK', serializers.RegistoPUTSerializer)
alerta_response = openapi.Response('OK', serializers.AlertPUTSerializer)


@swagger_auto_schema(method='get', responses={200: categoria_response})
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
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CategoriasDetalhe(APIView):
    """
    GET: Retorna uma categoria baseado num ID
    PATCH: Altera uma categoria baseado num ID
    DELETE: Elimina uma categoria baseado num ID
    """

    def get(self, request, categoria_id):
        try:
            categorias = Categoria.objects.get(pk=categoria_id)
        except Categoria.DoesNotExist:
            raise Http404
        serializer = serializers.CategoriaSerializer(categorias)
        return Response(serializer.data)

    def patch(self, request, categoria_id):
        categorias = Categoria.objects.get(pk=categoria_id)
        serializer = serializers.CategoriaSerializer(categorias, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, categoria_id):
        try:
            categorias = Categoria.objects.get(pk=categoria_id)
        except Categoria.DoesNotExist:
            raise Http404
        categorias.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: subcategoria_response})
@swagger_auto_schema(method='post', responses={200: subcategoria_response})
@api_view(['GET', 'POST'])
def criar_subcategoria(request):
    """
    GET: Retorna todas as sub_categorias
    POST: Insere uma nova sub_categoria
    """
    if request.method == 'GET':
        sub_categorias = SubCategoria.objects.all()
        serializer = serializers.SubCategoriaSerializer(sub_categorias, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.SubCategoriaPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class SubCategoriaDetalhe(APIView):
    """
    GET: Retorna uma subcategoria baseado num ID
    PATCH: Altera uma subcategoria baseado num ID
    DELETE: Elimina uma subcategoria baseado num ID
    """

    def get(self, request, subcategoria_id):
        try:
            subcategorias = SubCategoria.objects.get(pk=subcategoria_id)
        except SubCategoria.DoesNotExist:
            raise Http404
        serializer = serializers.SubCategoriaSerializer(subcategorias)
        return Response(serializer.data)

    def patch(self, request, subcategoria_id):
        subcategorias = SubCategoria.objects.get(pk=subcategoria_id)
        serializer = serializers.SubCategoriaPUTSerializer(subcategorias, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subcategoria_id):
        try:
            subcategorias = SubCategoria.objects.get(pk=subcategoria_id)
        except Categoria.DoesNotExist:
            raise Http404
        subcategorias.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: planeamento_response})
@swagger_auto_schema(method='post', responses={200: planeamento_response})
@api_view(['GET', 'POST'])
def criar_planeamento(request):
    """
    GET: Retorna todos os planeamentos
    POST: Insere um novo planeamento
    """
    if request.method == 'GET':
        planeamentos = Planeamento.objects.all()
        serializer = serializers.PlaneamentoSerializer(planeamentos, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.PlaneamentoPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class PlaneamentosDetalhe(APIView):
    """
    GET: Retorna um planemanento baseado num ID
    PATCH: Altera um planemanento baseado num ID
    DELETE: Elimina um planemanento baseado num ID
    """

    def get(self, request, planeamento_id):
        try:
            planeamento = Planeamento.objects.get(pk=planeamento_id)
        except Planeamento.DoesNotExist:
            raise Http404
        serializer = serializers.PlaneamentoSerializer(planeamento)
        return Response(serializer.data)

    def patch(self, request, planeamento_id):
        planeamento = Planeamento.objects.get(pk=planeamento_id)
        serializer = serializers.PlaneamentoPUTSerializer(planeamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, planeamento_id):
        try:
            planeamento = Planeamento.objects.get(pk=planeamento_id)
        except Planeamento.DoesNotExist:
            raise Http404
        planeamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: conta_response})
@swagger_auto_schema(method='post', responses={200: conta_response})
@api_view(['GET', 'POST'])
def criar_conta(request):
    """
    GET: Retorna todas as contas
    POST: Insere uma nova conta
    """
    if request.method == 'GET':
        contas = Conta.objects.all()
        serializer = serializers.ContaSerializer(contas, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.ContaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ContasList(APIView):
    """
    GET: Retorna uma conta baseado num ID
    PATCH: Altera uma conta baseado num ID
    DELETE: Elimina uma conta baseado num ID
    """

    def get(self, request, conta_id):
        try:
            contas = Conta.objects.get(pk=conta_id)
        except Conta.DoesNotExist:
            raise Http404
        serializer = serializers.ContaSerializer(contas)
        return Response(serializer.data)

    def patch(self, request, conta_id):
        contas = Conta.objects.get(pk=conta_id)
        serializer = serializers.ContaSerializer(contas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, conta_id):
        try:
            conta = Conta.objects.get(pk=conta_id)
        except Conta.DoesNotExist:
            raise Http404
        conta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: investimento_response})
@swagger_auto_schema(method='post', responses={200: investimento_response})
@api_view(['GET', 'POST'])
def criar_invest(request):
    """
    GET: Retorna todos os investimentos
    POST: Cria um novo investimento
    """
    if request.method == 'GET':
        invest = Invest.objects.all()
        serializer = serializers.InvestSerializer(invest, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.InvestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class InvestDetalhes(APIView):
    """
    GET: Retorna um investimento baseado num ID
    PATCH: Altera um investimento baseado num ID
    DELETE: Elimina um investimento baseado num ID
    """

    def get(self, request, invest_id):
        try:
            invest = Invest.objects.get(pk=invest_id)
        except Invest.DoesNotExist:
            raise Http404
        serializer = serializers.InvestSerializer(invest)
        return Response(serializer.data)

    def patch(self, request, invest_id):
        invest = Invest.objects.get(pk=invest_id)
        serializer = serializers.InvestSerializer(invest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, invest_id):
        try:
            invest = Invest.objects.get(pk=invest_id)
        except Invest.DoesNotExist:
            raise Http404
        invest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: registo_response})
@swagger_auto_schema(method='post', responses={200: registo_response})
@api_view(['GET', 'POST'])
def criar_registo(request):
    """
    GET: Retorna todos os registos
    POST: Cria um novo registo
    """
    if request.method == 'GET':
        registo = Registo.objects.all()
        serializer = serializers.RegistoSerializer(registo, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.RegistoPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class RegistoDetalhes(APIView):
    """
    GET: Retorna um registo baseado num ID
    PATCH: Altera um registo baseado num ID
    DELETE: Elimina um registo baseado num ID
    """

    def get(self, request, registo_id):
        try:
            registo = Registo.objects.get(pk=registo_id)
        except Registo.DoesNotExist:
            raise Http404
        serializer = serializers.RegistoSerializer(registo)
        return Response(serializer.data)

    def patch(self, request, registo_id):
        registo = Registo.objects.get(pk=registo_id)
        serializer = serializers.RegistoPUTSerializer(registo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, registo_id):
        try:
            registo = Registo.objects.get(pk=registo_id)
        except Registo.DoesNotExist:
            raise Http404
        registo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: alerta_response})
@swagger_auto_schema(method='post', responses={200: alerta_response})
@api_view(['GET', 'POST'])
def criar_alert(request):
    """
    GET: Retorna todos os alertas
    POST: Cria um novo alertas
    """
    if request.method == 'GET':
        alert = Registo.objects.all()
        serializer = serializers.AlertSerializer(alert, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.AlertPUTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class AlertaDetalhes(APIView):
    """
    GET: Retorna um alerta baseado num ID
    PATCH: Altera um alerta baseado num ID
    DELETE: Elimina um alerta baseado num ID
    """

    def get(self, request, alert_id):
        try:
            alert = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            raise Http404
        serializer = serializers.AlertSerializer(alert)
        return Response(serializer.data)

    def patch(self, request, alert_id):
        try:
            alert = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            raise Http404
        serializer = serializers.AlertPUTSerializer(alert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, alert_id):
        try:
            alert = Alert.objects.get(pk=alert_id)
        except Alert.DoesNotExist:
            raise Http404
        alert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
