"""Claim filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from clinica.models import Claim


class ClaimFilter(filters.FilterSet):
    class Meta:
        model = Claim
        fields = (
            'id',
            'principal',
            'id_aseguranza',
            'aseguranza',
            'paciente',
            'medico',
            'fecha_envio',
            'fecha_finalizacion',
            'fecha_reenviado',
            'medio_de_envio',
            'estado_de_pago',
            'estado',
            'notas',
        )