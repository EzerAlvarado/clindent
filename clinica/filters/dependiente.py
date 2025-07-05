"""Dependiente filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Dependiente


class DependienteFilter(filters.FilterSet):
    class Meta:
        model = Dependiente
        fields = (
            'id',
            'titular',
            'dependiente',
        )