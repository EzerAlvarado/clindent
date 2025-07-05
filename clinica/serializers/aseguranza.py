"""Aseguranza serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Aseguranza

class AseguranzaModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Aseguranza
    """

    class Meta:
        model = Aseguranza
        fields = (
            'id',
            'nombre',
        )
        read_only_fields = ('id',)