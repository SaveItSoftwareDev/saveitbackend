from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
# Create your views here.

from rest_framework import viewsets
from .models import Perfil
from .serializers import PerfilSerializer

"""
class PerfilListView(ListAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDetailView(RetrieveAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilCreateView(CreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilUpdateView(UpdateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDeleteView(DestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    
"""

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()