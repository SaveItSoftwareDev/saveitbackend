from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Perfil, Categoria, SubCategoria, Planeamento, Conta, Invest, Registo, Alert
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'user', 'idade', 'email', 'cidade', 'profissao']

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