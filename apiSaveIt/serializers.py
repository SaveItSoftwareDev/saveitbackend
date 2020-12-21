from rest_framework import serializers
from .models import Perfil, Categoria, SubCategoria, Planeamento, Conta

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
        fields = ['id_utilizador', 'nome', 'saldoIncial', 'tipo']