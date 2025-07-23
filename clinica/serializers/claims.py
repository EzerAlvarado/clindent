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
        
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.paciente:
            data['paciente'] = {
                'id': instance.paciente.id,
                'nombre_completo': instance.paciente.nombre_completo,
            }

        if instance.aseguranza:
            data['aseguranza'] = {
                'id': instance.aseguranza.id,
                'nombre': instance.aseguranza.nombre,
            }

        return data