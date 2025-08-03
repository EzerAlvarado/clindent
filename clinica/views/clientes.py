from django.shortcuts import render

# Create your views here.
#models
from clinica.models import Cliente
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.clientes import ClienteModelSerializer, ClienteCreateSerializer
#filters
from clinica.filters.clientes import ClienteFilter

class ClienteViewSet(viewsets.ModelViewSet):
    """
    View de clientes
    Maneja CRUD con lógica mejorada para dependientes
    """
    queryset=Cliente.objects.all()
    serializer_class = ClienteModelSerializer
    filterset_class = ClienteFilter
    
    def get_serializer_class(self):
        """
        Usar serializer específico para crear clientes
        """
        if self.action == 'create':
            return ClienteCreateSerializer
        return ClienteModelSerializer