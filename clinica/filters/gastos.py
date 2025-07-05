"""Gasto filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Gasto


class GastoFilter(filters.FilterSet):
    class Meta:
        model = Gasto
        fields = (
            'id',
            'cliente',
            'concepto',
            'monto',
            'fecha',
        )