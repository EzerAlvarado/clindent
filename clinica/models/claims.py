from django.db import models
from django.core.exceptions import ValidationError

class Claim(models.Model):
    
    def clean(self):
        if self.claim_enviado and not self.claim_enviado.name.lower().endswith('.pdf'):
            raise ValidationError("claim enviado debe ser un archivo PDF")
        
        if self.pagos and not self.pagos.name.lower().endswith('.pdf'):
            raise ValidationError("pagos debe ser un archivo PDF")

    principal = models.ForeignKey(
        'clinica.Cliente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='claims'
    )
    
    id_aseguranza = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text='id de con el que esta ligado la aseguranza',
    )

    aseguranza = models.ForeignKey(
        'clinica.Aseguranza',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING, 
        related_name='claims'
    )
    
    paciente = models.ForeignKey(
        'clinica.Cliente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='claims_paciente'
    )
    
    medico = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text='Nombre del medico',
    )
    
    claim_enviado = models.FileField(
        upload_to='claims/enviados/',
        null=True,
        blank=True
        )
    
    pagos = models.FileField(
        upload_to='claims/pagos/',
        null=True,
        blank=True
        )
    
    fecha_envio = models.DateField(
        null=True,
        blank=True
    )
    
    fecha_finalizacion = models.DateField(
        null=True,
        blank=True
    )
    
    fecha_reenviado = models.DateField(
        null=True,
        blank=True
    )
    
    medio_de_envio = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    estado_de_pago = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    estado = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    
    notas = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'claims'
        ordering = ['pk']
        verbose_name = 'Claim'
        verbose_name_plural = 'Claims'
        permissions = [
            ['autorizar_claims', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_claims', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Principal: {self.principal} | Id Aseguranza: {self.id_aseguranza}"