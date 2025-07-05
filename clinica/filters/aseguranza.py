"""Aseguranza filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Aseguranza


class AseguranzaFilter(filters.FilterSet):
    class Meta:
        model = Aseguranza
        fields = (
            'id',
            'nombre',
        )