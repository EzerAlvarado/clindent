from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Gasto
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.gastos import GastoModelSerializer
#filters
from clinica.filters.gastos import GastoFilter

class GastoViewSet(viewsets.ModelViewSet):
    """
    View de Gastos
    Maneja CRUD
    """
    queryset=Gasto.objects.all()
    serializer_class = GastoModelSerializer
    filterset_class = GastoFilter