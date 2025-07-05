"""Dependiente serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Dependiente

class DependienteModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Dependiente
    """

    class Meta:
        model = Dependiente
        fields = (
            'id',
            'titular',
            'dependiente',
        )
        read_only_fields = ('id',)