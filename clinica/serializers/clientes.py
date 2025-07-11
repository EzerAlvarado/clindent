"""Cliente serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Cliente

class ClienteModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Cliente
    """

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
            'numero_celular',
            'grupo',
            'trabajo',
            'numero_telefonico',
            'direccion',
            'aseguranza',
            'cobertura_dental',
        )
        read_only_fields = ('id',)