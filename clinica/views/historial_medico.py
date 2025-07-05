from django.shortcuts import render

# Create your views here.
#models
from clinica.models import HistorialMedico
#rest
from rest_framework import viewsets
#utilities
from clinica.serializers.historial_medico import HistorialMedicoModelSerializer
#filters
from clinica.filters.historial_medico import HistorialMedicoFilter

class HistorialMedicoViewSet(viewsets.ModelViewSet):
    """
    View de HistorialMedicos
    Maneja CRUD
    """
    queryset=HistorialMedico.objects.all()
    serializer_class = HistorialMedicoModelSerializer
    filterset_class = HistorialMedicoFilter