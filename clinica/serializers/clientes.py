"""Cliente serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Cliente

class ClienteDependienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_de_nacimiento', 'nombre_completo', 'correo', 'numero_celular'
        )

class ClienteModelSerializer(serializers.ModelSerializer):
    titular = ClienteDependienteSerializer()
    dependientes = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = (
            'id',
            'id_aseguranza',
            'es_titular',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_de_nacimiento',
            'nombre_completo',
            'correo',
            'numero_celular',
            'grupo',
            'trabajo',
            'numero_telefonico',
            'direccion',
            'aseguranza',
            'titular',
            'cobertura_dental',
            'dependientes',
        )
        read_only_fields = ('id',)

    def get_dependientes(self, obj):
        dependientes = obj.obtener_dependientes()
        return ClienteDependienteSerializer(dependientes, many=True).data