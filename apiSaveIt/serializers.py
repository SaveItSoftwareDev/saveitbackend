from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'primeiro_nome', 'ultimo_nome', 'idade', 'email', 'cidade', 'profissao']