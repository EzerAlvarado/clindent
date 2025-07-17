"""Cliente filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Cliente


class ClienteFilter(filters.FilterSet):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'id_aseguranza',
            'es_titular',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'nombre_completo',
            'correo',
            'titular',
            'numero_celular',
            'grupo',
            'trabajo',
            'numero_telefonico',
            'direccion',
            'aseguranza',
            'cobertura_dental',
        )