from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
# Create your views here.

from rest_framework import viewsets
from .models import Perfil
from .serializers import PerfilSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()


class PerfilView(APIView):

    serializer_class = PerfilSerializer

    def get(self, request):
            id = [{"Primeiro Nome:": id.primeiro_nome, "Email: ": id.email}
            for i in Perfil.objects.all()]
            return Response(id)

    def post(self, request):

        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)