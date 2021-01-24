from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import Categoria, SubCategoria, Planeamento, Conta, Invest, Registo, Alert
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user', 'username',)


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
        fields = ('id_user', 'token', 'username', 'password')


class PlaneamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeamento
        fields = ['id_planeamento', 'montante_limite', 'categoria', 'sub_categoria', 'prazo']


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id_conta', 'nome', 'saldo', 'tipo']


class InvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invest
        fields = ['id_invest', 'nome', 'montante', 'numero', 'data']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id_categoria", "nome")


class SubCategoriaSerializer(serializers.ModelSerializer):
    id_categoria = CategoriaSerializer(many=False)

    class Meta:
        model = SubCategoria
        fields = ['id_subcategoria', 'id_categoria', 'nome']


class RegistoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=False)
    sub_categoria = SubCategoriaSerializer(many=False)
    id_conta = ContaSerializer(many=False)

    class Meta:
        model = Registo
        fields = ['id_conta', 'tipo', 'descricao', 'categoria', 'sub_categoria', 'montante', 'data']


class AlertSerializer(serializers.ModelSerializer):
    id_planeamento = PlaneamentoSerializer(many=False)
    id_categoria = CategoriaSerializer(many=False)
    id_sub_categoria = SubCategoriaSerializer(many=False)

    class Meta:
        model = Alert
        fields = ['id_planeamento', 'id_categoria', 'id_sub_categoria', 'descricao', 'dataInicial', 'dataFinal',
                  'montante', 'montanteLimite']
