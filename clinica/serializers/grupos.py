"""Grupo serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Grupo

class GrupoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Grupo
    """

    class Meta:
        model = Grupo
        fields = (
            'id',
            'nombre',
            'servicios',
        )
        read_only_fields = ('id',)