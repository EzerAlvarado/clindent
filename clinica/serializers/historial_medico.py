"""HistorialMedico serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import HistorialMedico

class HistorialMedicoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un HistorialMedico
    """

    class Meta:
        model = HistorialMedico
        fields = (
            'id',
            'cliente',
            'descripcion',
            'costo',
            'cobertura',
            'deducible',
            'reclamo_enviado',
            'fecha',
        )
        read_only_fields = ('id',)