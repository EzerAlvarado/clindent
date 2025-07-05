from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Cliente
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.clientes import ClienteModelSerializer
#filters
from clinica.filters.clientes import ClienteFilter

class ClienteViewSet(viewsets.ModelViewSet):
    """
    View de clientes
    Maneja CRUD
    """
    queryset=Cliente.objects.all()
    serializer_class = ClienteModelSerializer
    filterset_class = ClienteFilter