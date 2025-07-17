"""Claim serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Claim

class ClaimModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Claim
    """

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
            'claim_enviado',
            'pagos',
            'estado_de_pago',
            'estado',
            'notas',
        )
        read_only_fields = ('id',)