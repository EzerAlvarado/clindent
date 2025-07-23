"""HistorialMedico filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import HistorialMedico


class HistorialMedicoFilter(filters.FilterSet):
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