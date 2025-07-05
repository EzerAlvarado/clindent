"""Gasto filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Usuario


class UsuarioFilter(filters.FilterSet):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'clave',
            'puede_editar',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
        )