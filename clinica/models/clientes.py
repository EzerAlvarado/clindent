from django.db import models

class Cliente(models.Model):
    """
    Modelo para los clientes de clinica
    """
    
    id_aseguranza = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text='id de con el que esta ligado la aseguranza',
    )
    
    es_titular = models.BooleanField(
        default=False,
        help_text='Indica si es el principal de la cuenta o dependiente'
    )
    
    nombre = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Nombre del cliente'
    )
    
    apellido_paterno = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Apellido paterno del cliente'
    )
    
    apellido_materno = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Apellido materno del cliente'
    )
    
    nombre_completo = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text='Nombre concatenado del cliente'
    )
    
    correo = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    
    numero_celular = models.BigIntegerField(
        null=True,
        blank=True
    )
    
    fecha_de_nacimiento = models.DateField(
        null=True,
        blank=True,
    )
    
    grupo = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Grupo del cliente')
    
    trabajo = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Trabajo')
    
    numero_telefonico = models.BigIntegerField(
        null=True,
        blank=True
    )
    
    direccion = models.TextField(
        null=True,
        blank=True
    )
        
    aseguranza = models.ForeignKey(
        'clinica.Aseguranza',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING, 
        related_name='clientes')
    
    cobertura_dental = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Campo editable para la cantidad que dinero disponible por el cliente')
    
    titular = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dependientes')
    
    class Meta:
        db_table = 'clientes'
        ordering = ['pk']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        permissions = [
            ['autorizar_cliente', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_cliente', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]
        indexes = [
            models.Index(fields=['nombre'], name='idx_nombre'),
            models.Index(fields=['apellido_paterno'], name='idx_apellido_paterno'),
            models.Index(fields=['apellido_materno'], name='idx_apellido_materno'),
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Paciente: {self.nombre} | ID Aseguranza : {self.id_aseguranza}"

    def obtener_dependientes(self):
        """
        Obtiene los dependientes del cliente:
        - Si es titular: retorna sus dependientes directos
        - Si es dependiente: retorna los dependientes de su titular (incluyéndose a sí mismo)
        """
        if self.es_titular:
            return self.dependientes.all().order_by('id')
        elif self.titular:
            return self.titular.dependientes.all().order_by('id')
        return []
    
    def obtener_titular(self):
        """
        Obtiene el titular del cliente:
        - Si es titular: retorna None
        - Si es dependiente: retorna su titular
        """
        if self.es_titular:
            return None
        return self.titular
    
    def es_dependiente_de(self, cliente):
        """
        Verifica si este cliente es dependiente del cliente especificado
        """
        if not self.es_titular and self.titular:
            return self.titular == cliente
        return False
    
    def tiene_dependientes(self):
        """
        Verifica si el cliente tiene dependientes
        """
        if self.es_titular:
            return self.dependientes.exists()
        return False
    
    def get_familia_completa(self):
        """
        Obtiene toda la familia (titular + dependientes)
        """
        if self.es_titular:
            # Si es titular, retorna él mismo + sus dependientes
            familia = [self] + list(self.dependientes.all())
        elif self.titular:
            # Si es dependiente, retorna su titular + todos los dependientes del titular
            familia = [self.titular] + list(self.titular.dependientes.all())
        else:
            # Cliente sin relación familiar
            familia = [self]
        
        return sorted(familia, key=lambda x: x.id)