"""Gasto serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Gasto

class GastoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Gasto
    """

    class Meta:
        model = Gasto
        fields = (
            'id',
            'cliente',
            'concepto',
            'monto',
            'fecha',
        )
        read_only_fields = ('id',)