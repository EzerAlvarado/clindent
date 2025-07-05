from django.shortcuts import render

# Create your views here.
#rest
from rest_framework import viewsets
#models
from clinica.models import Dependiente
#utilities
from clinica.serializers.dependiente import DependienteModelSerializer
#filters
from clinica.filters.dependiente import DependienteFilter

class DependienteViewSet(viewsets.ModelViewSet):
    """
    View de Dependientes
    Maneja CRUD
    """
    queryset=Dependiente.objects.all()
    serializer_class = DependienteModelSerializer
    filterset_class = DependienteFilter