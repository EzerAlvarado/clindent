"""Aseguranza serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Aseguranza

#utils
from clinica.serializers.grupos import GrupoModelSerializer

class AseguranzaModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Aseguranza
    """

    class Meta:
        model = Aseguranza
        fields = (
            'id',
            'servicios',
            'grupos',
            'nombre',
        )
        read_only_fields = ('id',)
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['grupos'] = GrupoModelSerializer(instance.grupos.all(), many=True).data
        return data