from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Grupo
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.grupos import GrupoModelSerializer
#filters
from clinica.filters.grupos import GrupoFilter

class GrupoViewSet(viewsets.ModelViewSet):
    """
    View de Grupos
    Maneja CRUD
    """
    queryset=Grupo.objects.all()
    serializer_class = GrupoModelSerializer
    filterset_class = GrupoFilter