from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Aseguranza
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.aseguranza import AseguranzaModelSerializer
#filters
from clinica.filters.aseguranza import AseguranzaFilter

class AseguranzaViewSet(viewsets.ModelViewSet):
    """
    View de Aseguranzas
    Maneja CRUD
    """
    queryset=Aseguranza.objects.all()
    serializer_class = AseguranzaModelSerializer
    filterset_class = AseguranzaFilter