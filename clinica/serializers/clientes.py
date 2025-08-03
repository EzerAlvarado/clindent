"""Cliente serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from clinica.models import Cliente

class ClienteDependienteSerializer(serializers.ModelSerializer):
    """Serializer para mostrar información básica de dependientes"""
    class Meta:
        model = Cliente
        fields = (
            'id', 'nombre', 'apellido_paterno', 'apellido_materno', 
            'fecha_de_nacimiento', 'nombre_completo', 'correo', 
            'numero_celular', 'es_titular'
        )

class ClienteCreateSerializer(serializers.ModelSerializer):
    """Serializer específico para crear clientes"""
    
    titular = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.filter(es_titular=True), 
        allow_null=True, 
        required=False,
        help_text='ID del cliente titular (solo para dependientes)'
    )

    class Meta:
        model = Cliente
        fields = (
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
        )

    def validate(self, data):
        """
        Validación personalizada para asegurar consistencia en las relaciones
        """
        es_titular = data.get('es_titular', False)
        titular = data.get('titular')
        
        # Si es titular, no debe tener un titular asignado
        if es_titular and titular:
            raise serializers.ValidationError(
                "Un cliente titular no puede tener un titular asignado."
            )
        
        # Si no es titular, debe tener un titular asignado
        if not es_titular and not titular:
            raise serializers.ValidationError(
                "Un cliente dependiente debe tener un titular asignado."
            )
        
        return data

class ClienteModelSerializer(serializers.ModelSerializer):
    """Serializer principal para clientes con manejo mejorado de dependientes"""
    
    # Campo para POST: acepta solo el ID del titular
    titular = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), 
        allow_null=True, 
        required=False,
        help_text='ID del cliente titular (solo para dependientes)'
    )
    
    # Campo para GET: muestra los dependientes del cliente
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
        read_only_fields = ('id', 'dependientes')

    def get_dependientes(self, obj):
        """
        Obtiene los dependientes del cliente:
        - Si es titular: retorna sus dependientes directos
        - Si es dependiente: retorna los dependientes de su titular (incluyéndose a sí mismo)
        """
        if obj.es_titular:
            # Si es titular, retorna sus dependientes directos
            dependientes = obj.dependientes.all().order_by('id')
        elif obj.titular:
            # Si es dependiente, retorna todos los dependientes de su titular
            dependientes = obj.titular.dependientes.all().order_by('id')
        else:
            # Si no tiene titular ni es titular, no tiene dependientes
            dependientes = []
        
        return ClienteDependienteSerializer(dependientes, many=True).data

    def validate(self, data):
        """
        Validación personalizada para asegurar consistencia en las relaciones
        """
        es_titular = data.get('es_titular', False)
        titular = data.get('titular')
        
        # Si es titular, no debe tener un titular asignado
        if es_titular and titular:
            raise serializers.ValidationError(
                "Un cliente titular no puede tener un titular asignado."
            )
        
        # Si no es titular, debe tener un titular asignado
        if not es_titular and not titular:
            raise serializers.ValidationError(
                "Un cliente dependiente debe tener un titular asignado."
            )
        
        # Si se asigna un titular, verificar que el titular sea realmente titular
        if titular and not titular.es_titular:
            raise serializers.ValidationError(
                "El cliente asignado como titular debe ser un titular válido."
            )
        
        return data

    def create(self, validated_data):
        """
        Crear cliente con validación adicional
        """
        # Si es dependiente, asegurar que el titular existe
        if not validated_data.get('es_titular', False):
            titular = validated_data.get('titular')
            if not titular:
                raise serializers.ValidationError(
                    "Los dependientes deben tener un titular asignado."
                )
        
        return super().create(validated_data)

    def to_representation(self, instance):
        """
        Personalizar la representación para GET:
        - titular: se muestra como objeto completo solo para dependientes
        - dependientes: se muestran como lista de objetos
        """
        data = super().to_representation(instance)
        
        # Para GET, mostrar el titular como objeto completo solo si es dependiente
        if instance.titular and not instance.es_titular:
            data['titular'] = ClienteDependienteSerializer(instance.titular).data
        else:
            data['titular'] = None
            
        return data
