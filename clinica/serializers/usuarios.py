"""Usuario serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Usuario

class UsuarioModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Usuario
    """

    class Meta:
        model = Usuario
        fields = (
            'id',
            'clave',
            'puede_editar',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
        )
        read_only_fields = ('id',)