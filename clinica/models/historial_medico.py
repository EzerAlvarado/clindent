from django.db import models

class HistorialMedico(models.Model):
    
    cliente = models.ForeignKey(
        'clinica.Cliente',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING, 
        related_name='tratamientos')
    
    fecha = models.DateField(
        help_text='Fecha del tratamiento',
        null=True,
        blank=True,
        )
    
    descripcion = models.TextField(
        help_text='Descripción del procedimiento realizado',
        null=True,
        blank=True,)
    
    costo = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Costo del procedimiento')
    
    reclamo_enviado = models.BooleanField(
        default=False,
        help_text='Indica si ya se envió la información a la aseguradora')

    
    class Meta:
        db_table = 'historial_medico'
        ordering = ['pk']
        verbose_name = 'Historial Medico'
        verbose_name_plural = 'Historial Medicos'
        permissions = [
            ['autorizar_historial_medico', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_historial_medico', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Paciente: {self.cliente} | Fecha : {self.fecha} | Reclamo enviado {self.reclamo_enviado}"