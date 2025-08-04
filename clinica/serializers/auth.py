"""Serializers para autenticación."""

from django.contrib.auth import authenticate
from rest_framework import serializers
from clinica.models import Usuario

class LoginSerializer(serializers.Serializer):
    """Serializer para login de usuarios."""
    
    username = serializers.CharField(
        max_length=150,
        help_text='Nombre de usuario'
    )
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        help_text='Contraseña del usuario'
    )

    def validate(self, data):
        """Validar credenciales de usuario."""
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        'La cuenta de usuario está deshabilitada.'
                    )
                data['user'] = user
                return data
            else:
                raise serializers.ValidationError(
                    'Credenciales inválidas. Por favor, verifica tu usuario y contraseña.'
                )
        else:
            raise serializers.ValidationError(
                'Debe proporcionar tanto el nombre de usuario como la contraseña.'
            )

class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer para mostrar información del usuario."""
    
    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'clave',
            'puede_editar',
            'es_admin',
            'is_active',
            'date_joined',
        )
        read_only_fields = ('id', 'date_joined')

class ChangePasswordSerializer(serializers.Serializer):
    """Serializer para cambiar contraseña."""
    
    old_password = serializers.CharField(
        max_length=128,
        write_only=True,
        help_text='Contraseña actual'
    )
    new_password = serializers.CharField(
        max_length=128,
        write_only=True,
        help_text='Nueva contraseña'
    )
    confirm_password = serializers.CharField(
        max_length=128,
        write_only=True,
        help_text='Confirmar nueva contraseña'
    )

    def validate(self, data):
        """Validar que las contraseñas coincidan."""
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError(
                'Las contraseñas nuevas no coinciden.'
            )
        return data

    def validate_old_password(self, value):
        """Validar que la contraseña actual sea correcta."""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                'La contraseña actual es incorrecta.'
            )
        return value 