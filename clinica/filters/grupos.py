"""Grupo filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Grupo


class GrupoFilter(filters.FilterSet):
    class Meta:
        model = Grupo
        fields = (
            'id',
            'nombre',
        )