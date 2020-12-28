from rest_framework import serializers
from .models import Perfil, Categoria, SubCategoria, Planeamento, Conta, Invest, Registo, Alert


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'primeiro_nome', 'ultimo_nome', 'idade', 'email', 'cidade', 'profissao']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_utilizador', 'nome']

class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = ['id_utilizador', 'id_categoria', 'nome']

class PlaneamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeamento
        fields = ['id_utilizador', 'montante_limite', 'categoria', 'sub_categoria', 'prazo']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id_utilizador', 'nome', 'saldo', 'tipo']

class InvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invest
        fields = ['id_utilizador', 'nome', 'montante', 'numero', 'data']

class RegistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registo
        fields = ['id_conta', 'id_utilizador', 'tipo', 'descricao', 'categoria', 'sub_categoria', 'montante', 'data']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id_planeamento', 'id_utilizador', 'id_categoria', 'id_sub_categoria', 'descricao', 'dataInicial', 'dataFinal', 'montante', 'montanteLimite']