from django.db import models

class Aseguranza(models.Model):
    """
    Modelo de Aseguranza
    """  
    nombre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Nombre de la aseguranza')
    
    grupo = models.CharField(
        max_length=150,
        null=True,
        blank=True
        )
    
    servicios = models.TextField(
        null=True,
        blank=True,
    )
    
    grupo = models.ForeignKey(
        'clinica.Grupo',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING, 
        related_name='aseguranzas')
    
    class Meta:
        db_table = 'aseguranzas'
        ordering = ['pk']
        verbose_name = 'Aseguranza'
        verbose_name_plural = 'Aseguranzas'
        permissions = [
            ['autorizar_aseguranza', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_aseguranza', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre: {self.nombre}  "
