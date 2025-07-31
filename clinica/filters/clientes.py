"""Cliente filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Cliente


class ClienteFilter(filters.FilterSet):
    nombre = filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    apellido_paterno = filters.CharFilter(field_name='apellido_paterno', lookup_expr='icontains')
    apellido_materno = filters.CharFilter(field_name='apellido_materno', lookup_expr='icontains')
    class Meta:
        model = Cliente
        fields = (
            'id',
            'id_aseguranza',
            'es_titular',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_de_nacimiento',
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