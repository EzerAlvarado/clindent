from django.db import models

class Grupo(models.Model):
    
    nombre = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        )
    
    servicios = models.JSONField(
        null=True,
        blank=True,
        help_text='Este campo con contenido JSON para un proceso determinado.')

    class Meta:
        db_table = 'grupos'
        ordering = ['pk']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        permissions = [
            ['autorizar_grupos', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_grupos', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Grupo de la Aseguranza: {self.nombre}"