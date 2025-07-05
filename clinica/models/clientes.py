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
    
    es_principal = models.BooleanField(
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
    
    numero_celular = models.IntegerField(
        null=True,
        blank=True
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
    
    numero_telefonico = models.IntegerField(
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
    
    class Meta:
        db_table = 'clientes'
        ordering = ['pk']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        permissions = [
            ['autorizar_cliente', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_cliente', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Paciente: {self.nombre} | ID Aseguranza : {self.id_aseguranza}"